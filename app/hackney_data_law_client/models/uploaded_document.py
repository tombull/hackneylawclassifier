# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class UploadedDocument(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        UploadedDocument - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'owner_id': 'str',
            'created_at': 'datetime',
            'upload_time': 'datetime',
            'file_data': 'str',
            'case_record': 'CaseRecord',
            'related_document': 'RequiredDocument',
            'id': 'str',
            'v': 'float',
            'id': 'str'
        }

        self.attribute_map = {
            'owner_id': '_ownerId',
            'created_at': '_createdAt',
            'upload_time': 'uploadTime',
            'file_data': 'fileData',
            'case_record': 'caseRecord',
            'related_document': 'relatedDocument',
            'id': '_id',
            'v': '__v'
        }

        self._owner_id = None
        self._created_at = None
        self._upload_time = None
        self._file_data = None
        self._case_record = None
        self._related_document = None
        self._id = None
        self._v = None
        self._id = None

    @property
    def owner_id(self):
        """
        Gets the owner_id of this UploadedDocument.


        :return: The owner_id of this UploadedDocument.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """
        Sets the owner_id of this UploadedDocument.


        :param owner_id: The owner_id of this UploadedDocument.
        :type: str
        """
        self._owner_id = owner_id

    @property
    def created_at(self):
        """
        Gets the created_at of this UploadedDocument.


        :return: The created_at of this UploadedDocument.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this UploadedDocument.


        :param created_at: The created_at of this UploadedDocument.
        :type: datetime
        """
        self._created_at = created_at

    @property
    def upload_time(self):
        """
        Gets the upload_time of this UploadedDocument.


        :return: The upload_time of this UploadedDocument.
        :rtype: datetime
        """
        return self._upload_time

    @upload_time.setter
    def upload_time(self, upload_time):
        """
        Sets the upload_time of this UploadedDocument.


        :param upload_time: The upload_time of this UploadedDocument.
        :type: datetime
        """
        self._upload_time = upload_time

    @property
    def file_data(self):
        """
        Gets the file_data of this UploadedDocument.


        :return: The file_data of this UploadedDocument.
        :rtype: str
        """
        return self._file_data

    @file_data.setter
    def file_data(self, file_data):
        """
        Sets the file_data of this UploadedDocument.


        :param file_data: The file_data of this UploadedDocument.
        :type: str
        """
        self._file_data = file_data

    @property
    def case_record(self):
        """
        Gets the case_record of this UploadedDocument.


        :return: The case_record of this UploadedDocument.
        :rtype: CaseRecord
        """
        return self._case_record

    @case_record.setter
    def case_record(self, case_record):
        """
        Sets the case_record of this UploadedDocument.


        :param case_record: The case_record of this UploadedDocument.
        :type: CaseRecord
        """
        self._case_record = case_record

    @property
    def related_document(self):
        """
        Gets the related_document of this UploadedDocument.


        :return: The related_document of this UploadedDocument.
        :rtype: RequiredDocument
        """
        return self._related_document

    @related_document.setter
    def related_document(self, related_document):
        """
        Sets the related_document of this UploadedDocument.


        :param related_document: The related_document of this UploadedDocument.
        :type: RequiredDocument
        """
        self._related_document = related_document

    @property
    def id(self):
        """
        Gets the id of this UploadedDocument.


        :return: The id of this UploadedDocument.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UploadedDocument.


        :param id: The id of this UploadedDocument.
        :type: str
        """
        self._id = id

    @property
    def v(self):
        """
        Gets the v of this UploadedDocument.


        :return: The v of this UploadedDocument.
        :rtype: float
        """
        return self._v

    @v.setter
    def v(self, v):
        """
        Sets the v of this UploadedDocument.


        :param v: The v of this UploadedDocument.
        :type: float
        """
        self._v = v

    @property
    def id(self):
        """
        Gets the id of this UploadedDocument.


        :return: The id of this UploadedDocument.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UploadedDocument.


        :param id: The id of this UploadedDocument.
        :type: str
        """
        self._id = id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

