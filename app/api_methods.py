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

from hackney_law_data_client import *

config = Configuration()
config.host = HACKNEY_LAW_DATA_API_URL
config.api_key = { 'apikey': HACKNEY_LAW_DATA_API_KEY }
config.debug = DEBUG


# mes = SystemMessage()
# mes.message_name='test'
# mes.message='test'
# api = SystemMessageApi()
# api.create_system_message(mes)
