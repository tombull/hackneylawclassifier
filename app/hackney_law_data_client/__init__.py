from __future__ import absolute_import

# import models into sdk package
from .models._body_id_parameter import BodyIdParameter
from .models.case_record import CaseRecord
from .models.classification import Classification
from .models._config import Config
from .models.contact_item import ContactItem
from .models.document_state import DocumentState
from .models.generic_question import GenericQuestion
from .models.lawyer import Lawyer
from .models._permissions import Permissions
from .models.potential_answer import PotentialAnswer
from .models._providers import Providers
from .models.referral import Referral
from .models.related_link import RelatedLink
from .models.required_document import RequiredDocument
from .models._status import Status
from .models.system_message import SystemMessage
from .models.uploaded_document import UploadedDocument
from .models.uploaded_picture import UploadedPicture
from .models.user import User
from .models._users import Users
from .models.validation_error import ValidationError
from .models.validation_error_properties import ValidationErrorProperties
from .models._webhooks import Webhooks
from .models._webhooks_parameters import WebhooksParameters

# import apis into sdk package
from .apis.binary_api import BinaryApi
from .apis.case_record_api import CaseRecordApi
from .apis.classification_api import ClassificationApi
from .apis.contact_item_api import ContactItemApi
from .apis.document_state_api import DocumentStateApi
from .apis.generic_question_api import GenericQuestionApi
from .apis.lawyer_api import LawyerApi
from .apis.potential_answer_api import PotentialAnswerApi
from .apis.referral_api import ReferralApi
from .apis.related_link_api import RelatedLinkApi
from .apis.required_document_api import RequiredDocumentApi
from .apis.system_message_api import SystemMessageApi
from .apis.uploaded_document_api import UploadedDocumentApi
from .apis.uploaded_picture_api import UploadedPictureApi
from .apis.user_api import UserApi
from .apis.config_api import ConfigApi
from .apis.diagnostics_api import DiagnosticsApi
from .apis.permissions_api import PermissionsApi
from .apis.providers_api import ProvidersApi
from .apis.users_api import UsersApi
from .apis.webhooks_api import WebhooksApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
