"""The main API functions."""
from app import app, api
from flask_restful import Resource, reqparse, abort
from settings import HACKNEY_LAW_DATA_API_KEY
from settings import HACKNEY_LAW_DATA_API_URL
from settings import HACKNEY_LAW_MESSAGE_API_URL
from settings import HACKNEY_LAW_MESSAGE_API_KEY
from settings import CASE_RECORD_TIMEOUT_MINUTES
from settings import SYSTEM_NAME
from settings import SYSTEM_URL
from settings import FILE_UPLOAD_URL_PATTERN
from settings import PICTURE_TAKE_URL_PATTERN
from settings import DEBUG
import re
from datetime import datetime, timedelta
import string
import os
import pdb
import pytz
import requests
import json

from app.hackney_law_data_client import *

config = Configuration()
config.host = HACKNEY_LAW_DATA_API_URL
config.api_key = {'apikey': HACKNEY_LAW_DATA_API_KEY}
config.debug = DEBUG

telephoneregex = re.compile(r"\A\+?[\d\s\-]+\Z")

emailregex = re.compile(r"\A[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*" +
                        r"+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9]" +
                        r")?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\z")

systemmessageapi = SystemMessageApi()
system_messages = systemmessageapi.query_system_message()
messages = {}
for system_message in system_messages:
    messages[system_message.message_name] = system_message.message



intents = {
    'e61e18cf-e97e-4ec1-a51e-e80951e0ca83': 'Welfare',
    'df779cdf-504e-4487-92ed-c956197f43d7': 'Debt'
}

class ReceiveMessage(Resource):
    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(
            'from', dest='user_identifier', required=True,
            help='You must specify a user identifier.')
        parser.add_argument(
            'translated-body', dest='message_english', required=True,
            help='You must specify a message in English.')
        parser.add_argument(
            'original-language', dest='language', required=True,
            help='You must specify a language for the original message.')
        parser.add_argument('translated-body', dest='message_original', required=False)
        parser.add_argument('intentId', dest='intent_id', required=False)
        args = parser.parse_args()

        user = get_user(args)
        case = get_case_record(user)

        for pattern, function in transitions.iteritems():
            if re.match(pattern, case.case_state):
                function[0](user=user, case=case, incoming_message=args.message_english,
                    language=args.language.strip().lower(),
                    intent=args.intent_id, **function[1])

        contactitemapi = ContactItemApi()
        new_contact = ContactItem()
        new_contact.case_record = case
        new_contact.contact_time = datetime.now()
        new_contact.direction = False
        new_contact.language = args.language.strip().lower()
        new_contact.message_english = args.message_english
        new_contact.message_original = args.message_original or 'not applicable'
        contactitemapi.create_contact_item(new_contact)

        return {'message': 'success'}

api.add_resource(ReceiveMessage, '/receive')

def send_message_and_change_state(user, case, message, desired_state, **kwargs):
    if hasattr(message, '__call__'):
        message_to_send = message(user=user, case=case, message=message)
    else:
        message_to_send = message

    url = HACKNEY_LAW_MESSAGE_API_URL + 'sms/send'
    requests.post(url,
        json={'to': user.identifier,
            'body': message_to_send,
            'lang': user.default_language})

    caserecordapi = CaseRecordApi()
    caserecordapi.update_case_record(id=case.id, document={'case_state': desired_state})

    contactitemapi = ContactItemApi()
    new_contact = ContactItem()
    new_contact.case_record = case
    new_contact.contact_time = datetime.now()
    new_contact.direction = True
    new_contact.language = user.default_language
    new_contact.message_english = message_to_send
    new_contact.message_original = 'not applicable'
    contactitemapi.create_contact_item(new_contact)

def choose_initial_message(case):
    caserecordapi = CaseRecordApi()
    classification = caserecordapi.get_case_record_case_type(id=case.id)
    return classification.initial_advice

def classify(user, case, message, intent_id, **kwargs):
    #if case.case_state == 'classifyinitial':
    classify_stage = int(case.case_state[-1:])
    classificationapi = ClassificationApi()
    if intent_id in intents.keys():

        potential_classifications = classificationapi.query_classification(
            limit=1,
            conditions=r'{"name": "' + intents[intent_id] + '"}')
        if len(potential_classifications) > 0:
            potential_classification = potential_classifications[0]
            send_message_and_change_state(user=user, case=case,
                message='I think you need help with ' + classification.description + ' is that right?',
                desired_state = 'classifyask' + str(classify_stage))
            caserecordapi = CaseRecordApi()
            #caserecordapi.update_case_record(id=case.id, {'caseType': potential_classification})
            return
    if classify_stage > 2:
        message_to_send = messages['unknownfinal']
        potential_classifications = classificationapi.query_classification(sort='id')
        for potential_classification in potential_classifications:
            message_to_send = message_to_send + '\\r' + str(index) + '. ' + potential_classification.short_description
        message_to_send = message_to_send + '\\r' + str(len(potential_classifications) + 1) + '. Something else'
        send_message_and_change_state(user=user, case=case,
            message=message_to_send, desired_state='classifyfinal')
    else:
        send_message_and_change_state(user=user, case=case,
            message=messages['unknown'],
            desired_state = 'classify' + str(classify_stage + 1))

def classify_ask(user, case, message, **kwargs):
    if message.lower().strip() in ['yes', 'it is', 'positive', 'affirmative']:
        caserecordapi = CaseRecordApi()
        classification = caserecordapi.get_case_record_case_type(id=case.id)
        send_message_and_change_state(user=user, case=case, message=classification.initial_advice, desired_state='afterclassify')
        classificationapi = ClassificationApi()
        relatedlinks = classificationapi.get_classification_related_information(id=classification.id)
        for related in relatedlinks:
            send_message_and_change_state(user=user, case=case, message=related.description + ':' + related.url, desired_state='sendinglinks')
        send_message_and_change_state(user=user, case=case, message='We have asked a lawyer to have a look at your case and they will try and get back to you soon.', desired_state='complete')
    else:
        classify(user=user, case=case, message='', intent_id='')

def get_user(args):
    trimmed_user_identifier = args.user_identifier.strip()
    user_identifier_type = ''
    sanitised_user_identifier = trimmed_user_identifier
    sanitised_language = args.language.strip().lower()

    if telephoneregex.match(trimmed_user_identifier):
        user_identifier_type = 'tel'
    elif emailregex.match(trimmed_user_identifier):
        user_identifier_type = 'email'
        sanitised_user_identifier = trimmed_user_identifier.lower()
    else:
        abort(400, message={'user_identifier':
                            'You must specify either a telephone number ' +
                            'or an email address for the user identifier'})

    userapi = UserApi()
    matching_users = userapi.query_user(limit=1,
        conditions=r'{"identifier": "' + sanitised_user_identifier + '", '
                   +r'"identifierType": "' + user_identifier_type + '"}')

    if len(matching_users) < 1:
        new_user = User()
        new_user.identifier = sanitised_user_identifier
        new_user.identifier_type = user_identifier_type
        new_user.default_language = sanitised_language
        resulting_user = userapi.create_user(new_user)
    else:
        resulting_user = matching_users[0]

    if resulting_user.default_language != sanitised_language:
        resulting_user.default_language = sanitised_language
        userapi.update_user(id=user.id, document={'default_language': sanitised_language})

    return resulting_user

def get_case_record(user):
    userapi = UserApi()
    potential_case_records = userapi.get_user_case_records(id=user.id)
    for potential_case_record in potential_case_records:
        some_time_ago = datetime.now(pytz.utc) - timedelta(minutes=CASE_RECORD_TIMEOUT_MINUTES)
        if potential_case_record.start_time > some_time_ago:
            return potential_case_record
    caserecordapi = CaseRecordApi()
    new_case_record = CaseRecord()
    new_case_record.user = user
    new_case_record.start_time = datetime.now()
    new_case_record.case_state = 'initialise'
    return caserecordapi.create_case_record(new_case_record)

transitions = {
    'initialise': (send_message_and_change_state, {'message': messages['welcome'], 'desired_state': 'classify1'}),
    'classify\\d': (classify, {}),
    'classifyask\\d': (classify_ask, {}),
    'classified': (send_message_and_change_state, {'message': choose_initial_message, 'desired_state': 'initialmessagesent'})
}

# mes = SystemMessage()
# mes.message_name='test'
# mes.message='test'
# api = SystemMessageApi()
# api.create_system_message(mes)
