"""The main API functions."""
from app import app, api
from flask_restful import Resource, reqparse, abort
from settings import HACKNEY_LAW_DATA_API_KEY
from settings import HACKNEY_LAW_DATA_API_URL
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

from hackney_law_data_client import *

config = Configuration()
config.host = HACKNEY_LAW_DATA_API_URL
config.api_key = {'apikey': HACKNEY_LAW_DATA_API_KEY}
config.debug = DEBUG

telephoneregex = re.compile(r"\A\+?[\d\s\-]+\Z")

emailregex = re.compile(r"\A[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*" +
                        r"+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9]" +
                        r")?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\z")

class ReceiveMessage(Resource):
    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(
            'user_identifier', required=True,
            help='You must specify a user identifier.')
        parser.add_argument(
            'message_english', required=True,
            help='You must specify a message in English.')
        parser.add_argument(
            'language', required=True,
            help='You must specify a language for the original message.')
        parser.add_argument('message_original', required=False)
        args = parser.parse_args()

        user = get_user(args)
        case = get_case_record(user)

        return {'identifier': user.identifier, 'identifier_type': user.identifier_type, 'case': case.id}


api.add_resource(ReceiveMessage, '/receive')

def get_user(args):
    trimmed_user_identifier = args.user_identifier.strip()
    user_identifier_type = ''
    sanitised_user_identifier = trimmed_user_identifier
    sanitised_language = args.language.strip().lower()

    if telephoneregex.match(trimmed_user_identifier):
        user_identifier_type = 'telephone'
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


# mes = SystemMessage()
# mes.message_name='test'
# mes.message='test'
# api = SystemMessageApi()
# api.create_system_message(mes)
