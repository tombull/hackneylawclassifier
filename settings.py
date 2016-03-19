"""Configuration values."""

import os
HACKNEY_LAW_DATA_API_KEY = os.environ.get(
    "HACKNEY_LAW_DATA_API_KEY", "aN0IL6Y3wMOBJIsMoWEDVAxHXJCREcRnGgxGnSjeBMzda2mvKC")

MAILGUN_SECRET_API_KEY = os.environ.get(
    "MAILGUN_SECRET_API_KEY", "aN0IL6Y3wMOBJIsMoWEDVAxHXJCREcRnGgxGnSjeBMzda2mvKC")

HACKNEY_LAW_MESSAGE_API_KEY = os.environ.get(
    "HACKNEY_LAW_MESSAGE_API_KEY", "aN0IL6Y3wMOBJIsMoWEDVAxHXJCREcRnGgxGnSjeBMzda2mvKC")

API_AI_ACCESS_TOKEN = os.environ.get(
    "API_AI_ACCESS_TOKEN", "0e010641a9db48eb8f53079054de0526")

DEBUG = bool(int(os.environ.get("DEBUG", 1)))

SERVER_MODE = os.environ.get("SERVER_MODE", "dev")

PORT = int(os.environ.get("PORT", 5000))

API_AI_URL = os.environ.get(
    "API_AI_URL",
    "https://api.api.ai/v1/")

HACKNEY_LAW_DATA_API_URL = os.environ.get(
    "HACKNEY_LAW_DATA_API_URL",
    "https://pod-superb-hivepod-2625.herokuapp.com/api")

HACKNEY_LAW_MESSAGE_API_URL = os.environ.get(
    "HACKNEY_LAW_MESSAGE_API_URL",
    "http://law.mmt.me.uk/")

CASE_RECORD_TIMEOUT_MINUTES = int(
    os.environ.get("CASE_RECORD_TIMEOUT_MINUTES", 1440))

MAILGUN_DOMAIN_NAME = os.environ.get(
    "MAILGUN_DOMAIN_NAME", "iteralis.com")

EMAIL_FROM_ADDRESS_AND_NAME = os.environ.get(
    "EMAIL_FROM_ADDRESS_AND_NAME",
    "Hackney Law Centre <tom@iteralis.com>")

SYSTEM_NAME = os.environ.get(
    "SYSTEM_NAME", "Hackney Law Centre")

SYSTEM_URL = os.environ.get(
    "SYSTEM_URL", "https://localhost:3000/")

FILE_UPLOAD_URL_PATTERN = os.environ.get(
    "FILE_UPLOAD_URL_PATTERN",
    "http://localhost:3000/fileupload/||case_record_id||/" +
    "||required_document_id||")

PICTURE_TAKE_URL_PATTERN = os.environ.get(
    "PICTURE_TAKE_URL_PATTERN",
    "http://localhost:3000/picturetake/||case_record_id||/" +
    "||related_document_id||")
