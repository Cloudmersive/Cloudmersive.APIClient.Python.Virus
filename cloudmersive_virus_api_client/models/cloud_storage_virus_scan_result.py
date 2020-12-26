# coding: utf-8

"""
    virusapi

    The Cloudmersive Virus Scan API lets you scan files and content for viruses and identify security issues with content.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CloudStorageVirusScanResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'successful': 'bool',
        'clean_result': 'bool',
        'found_viruses': 'list[CloudStorageVirusFound]',
        'error_detailed_description': 'str',
        'file_size': 'int'
    }

    attribute_map = {
        'successful': 'Successful',
        'clean_result': 'CleanResult',
        'found_viruses': 'FoundViruses',
        'error_detailed_description': 'ErrorDetailedDescription',
        'file_size': 'FileSize'
    }

    def __init__(self, successful=None, clean_result=None, found_viruses=None, error_detailed_description=None, file_size=None):  # noqa: E501
        """CloudStorageVirusScanResult - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._clean_result = None
        self._found_viruses = None
        self._error_detailed_description = None
        self._file_size = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if clean_result is not None:
            self.clean_result = clean_result
        if found_viruses is not None:
            self.found_viruses = found_viruses
        if error_detailed_description is not None:
            self.error_detailed_description = error_detailed_description
        if file_size is not None:
            self.file_size = file_size

    @property
    def successful(self):
        """Gets the successful of this CloudStorageVirusScanResult.  # noqa: E501

        True if the operation of retrieving the file, and scanning it were successfully completed, false if the file could not be downloaded from cloud storage, or if the file could not be scanned.  Note that successful completion does not mean the file is clean; for the output of the virus scanning operation itself, use the CleanResult and FoundViruses parameters.  # noqa: E501

        :return: The successful of this CloudStorageVirusScanResult.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this CloudStorageVirusScanResult.

        True if the operation of retrieving the file, and scanning it were successfully completed, false if the file could not be downloaded from cloud storage, or if the file could not be scanned.  Note that successful completion does not mean the file is clean; for the output of the virus scanning operation itself, use the CleanResult and FoundViruses parameters.  # noqa: E501

        :param successful: The successful of this CloudStorageVirusScanResult.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def clean_result(self):
        """Gets the clean_result of this CloudStorageVirusScanResult.  # noqa: E501

        True if the scan contained no viruses, false otherwise  # noqa: E501

        :return: The clean_result of this CloudStorageVirusScanResult.  # noqa: E501
        :rtype: bool
        """
        return self._clean_result

    @clean_result.setter
    def clean_result(self, clean_result):
        """Sets the clean_result of this CloudStorageVirusScanResult.

        True if the scan contained no viruses, false otherwise  # noqa: E501

        :param clean_result: The clean_result of this CloudStorageVirusScanResult.  # noqa: E501
        :type: bool
        """

        self._clean_result = clean_result

    @property
    def found_viruses(self):
        """Gets the found_viruses of this CloudStorageVirusScanResult.  # noqa: E501

        Array of viruses found, if any  # noqa: E501

        :return: The found_viruses of this CloudStorageVirusScanResult.  # noqa: E501
        :rtype: list[CloudStorageVirusFound]
        """
        return self._found_viruses

    @found_viruses.setter
    def found_viruses(self, found_viruses):
        """Sets the found_viruses of this CloudStorageVirusScanResult.

        Array of viruses found, if any  # noqa: E501

        :param found_viruses: The found_viruses of this CloudStorageVirusScanResult.  # noqa: E501
        :type: list[CloudStorageVirusFound]
        """

        self._found_viruses = found_viruses

    @property
    def error_detailed_description(self):
        """Gets the error_detailed_description of this CloudStorageVirusScanResult.  # noqa: E501

        Detailed error message if the operation was not successful  # noqa: E501

        :return: The error_detailed_description of this CloudStorageVirusScanResult.  # noqa: E501
        :rtype: str
        """
        return self._error_detailed_description

    @error_detailed_description.setter
    def error_detailed_description(self, error_detailed_description):
        """Sets the error_detailed_description of this CloudStorageVirusScanResult.

        Detailed error message if the operation was not successful  # noqa: E501

        :param error_detailed_description: The error_detailed_description of this CloudStorageVirusScanResult.  # noqa: E501
        :type: str
        """

        self._error_detailed_description = error_detailed_description

    @property
    def file_size(self):
        """Gets the file_size of this CloudStorageVirusScanResult.  # noqa: E501

        Size in bytes of the file that was retrieved and scanned  # noqa: E501

        :return: The file_size of this CloudStorageVirusScanResult.  # noqa: E501
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this CloudStorageVirusScanResult.

        Size in bytes of the file that was retrieved and scanned  # noqa: E501

        :param file_size: The file_size of this CloudStorageVirusScanResult.  # noqa: E501
        :type: int
        """

        self._file_size = file_size

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(CloudStorageVirusScanResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CloudStorageVirusScanResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
