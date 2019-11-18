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

from cloudmersive_virus_api_client.models.virus_found import VirusFound  # noqa: F401,E501


class VirusScanAdvancedResult(object):
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
        'clean_result': 'bool',
        'contains_executable': 'bool',
        'contains_invalid_file': 'bool',
        'contains_script': 'bool',
        'contains_restricted_file_format': 'bool',
        'verified_file_format': 'str',
        'found_viruses': 'list[VirusFound]'
    }

    attribute_map = {
        'clean_result': 'CleanResult',
        'contains_executable': 'ContainsExecutable',
        'contains_invalid_file': 'ContainsInvalidFile',
        'contains_script': 'ContainsScript',
        'contains_restricted_file_format': 'ContainsRestrictedFileFormat',
        'verified_file_format': 'VerifiedFileFormat',
        'found_viruses': 'FoundViruses'
    }

    def __init__(self, clean_result=None, contains_executable=None, contains_invalid_file=None, contains_script=None, contains_restricted_file_format=None, verified_file_format=None, found_viruses=None):  # noqa: E501
        """VirusScanAdvancedResult - a model defined in Swagger"""  # noqa: E501

        self._clean_result = None
        self._contains_executable = None
        self._contains_invalid_file = None
        self._contains_script = None
        self._contains_restricted_file_format = None
        self._verified_file_format = None
        self._found_viruses = None
        self.discriminator = None

        if clean_result is not None:
            self.clean_result = clean_result
        if contains_executable is not None:
            self.contains_executable = contains_executable
        if contains_invalid_file is not None:
            self.contains_invalid_file = contains_invalid_file
        if contains_script is not None:
            self.contains_script = contains_script
        if contains_restricted_file_format is not None:
            self.contains_restricted_file_format = contains_restricted_file_format
        if verified_file_format is not None:
            self.verified_file_format = verified_file_format
        if found_viruses is not None:
            self.found_viruses = found_viruses

    @property
    def clean_result(self):
        """Gets the clean_result of this VirusScanAdvancedResult.  # noqa: E501

        True if the scan contained no viruses, false otherwise  # noqa: E501

        :return: The clean_result of this VirusScanAdvancedResult.  # noqa: E501
        :rtype: bool
        """
        return self._clean_result

    @clean_result.setter
    def clean_result(self, clean_result):
        """Sets the clean_result of this VirusScanAdvancedResult.

        True if the scan contained no viruses, false otherwise  # noqa: E501

        :param clean_result: The clean_result of this VirusScanAdvancedResult.  # noqa: E501
        :type: bool
        """

        self._clean_result = clean_result

    @property
    def contains_executable(self):
        """Gets the contains_executable of this VirusScanAdvancedResult.  # noqa: E501

        True if the scan contained an executable (application code), which can be a significant risk factor  # noqa: E501

        :return: The contains_executable of this VirusScanAdvancedResult.  # noqa: E501
        :rtype: bool
        """
        return self._contains_executable

    @contains_executable.setter
    def contains_executable(self, contains_executable):
        """Sets the contains_executable of this VirusScanAdvancedResult.

        True if the scan contained an executable (application code), which can be a significant risk factor  # noqa: E501

        :param contains_executable: The contains_executable of this VirusScanAdvancedResult.  # noqa: E501
        :type: bool
        """

        self._contains_executable = contains_executable

    @property
    def contains_invalid_file(self):
        """Gets the contains_invalid_file of this VirusScanAdvancedResult.  # noqa: E501

        True if the scan contained an invalid file (such as a PDF that is not a valid PDF, Word Document that is not a valid Word Document, etc.), which can be a significant risk factor  # noqa: E501

        :return: The contains_invalid_file of this VirusScanAdvancedResult.  # noqa: E501
        :rtype: bool
        """
        return self._contains_invalid_file

    @contains_invalid_file.setter
    def contains_invalid_file(self, contains_invalid_file):
        """Sets the contains_invalid_file of this VirusScanAdvancedResult.

        True if the scan contained an invalid file (such as a PDF that is not a valid PDF, Word Document that is not a valid Word Document, etc.), which can be a significant risk factor  # noqa: E501

        :param contains_invalid_file: The contains_invalid_file of this VirusScanAdvancedResult.  # noqa: E501
        :type: bool
        """

        self._contains_invalid_file = contains_invalid_file

    @property
    def contains_script(self):
        """Gets the contains_script of this VirusScanAdvancedResult.  # noqa: E501

        True if the scan contained a script (such as a PHP script, Python script, etc.) which can be a significant risk factor  # noqa: E501

        :return: The contains_script of this VirusScanAdvancedResult.  # noqa: E501
        :rtype: bool
        """
        return self._contains_script

    @contains_script.setter
    def contains_script(self, contains_script):
        """Sets the contains_script of this VirusScanAdvancedResult.

        True if the scan contained a script (such as a PHP script, Python script, etc.) which can be a significant risk factor  # noqa: E501

        :param contains_script: The contains_script of this VirusScanAdvancedResult.  # noqa: E501
        :type: bool
        """

        self._contains_script = contains_script

    @property
    def contains_restricted_file_format(self):
        """Gets the contains_restricted_file_format of this VirusScanAdvancedResult.  # noqa: E501

        True if the uploaded file is of a type that is not allowed based on the optional restrictFileTypes parameter, false otherwise; if restrictFileTypes is not set, this will always be false  # noqa: E501

        :return: The contains_restricted_file_format of this VirusScanAdvancedResult.  # noqa: E501
        :rtype: bool
        """
        return self._contains_restricted_file_format

    @contains_restricted_file_format.setter
    def contains_restricted_file_format(self, contains_restricted_file_format):
        """Sets the contains_restricted_file_format of this VirusScanAdvancedResult.

        True if the uploaded file is of a type that is not allowed based on the optional restrictFileTypes parameter, false otherwise; if restrictFileTypes is not set, this will always be false  # noqa: E501

        :param contains_restricted_file_format: The contains_restricted_file_format of this VirusScanAdvancedResult.  # noqa: E501
        :type: bool
        """

        self._contains_restricted_file_format = contains_restricted_file_format

    @property
    def verified_file_format(self):
        """Gets the verified_file_format of this VirusScanAdvancedResult.  # noqa: E501

        For file format verification-supported file formats, the contents-verified file format of the file.  Null indicates that the file format is not supported for contents verification.  If a Virus or Malware is found, this field will always be set to Null.  # noqa: E501

        :return: The verified_file_format of this VirusScanAdvancedResult.  # noqa: E501
        :rtype: str
        """
        return self._verified_file_format

    @verified_file_format.setter
    def verified_file_format(self, verified_file_format):
        """Sets the verified_file_format of this VirusScanAdvancedResult.

        For file format verification-supported file formats, the contents-verified file format of the file.  Null indicates that the file format is not supported for contents verification.  If a Virus or Malware is found, this field will always be set to Null.  # noqa: E501

        :param verified_file_format: The verified_file_format of this VirusScanAdvancedResult.  # noqa: E501
        :type: str
        """

        self._verified_file_format = verified_file_format

    @property
    def found_viruses(self):
        """Gets the found_viruses of this VirusScanAdvancedResult.  # noqa: E501

        Array of viruses found, if any  # noqa: E501

        :return: The found_viruses of this VirusScanAdvancedResult.  # noqa: E501
        :rtype: list[VirusFound]
        """
        return self._found_viruses

    @found_viruses.setter
    def found_viruses(self, found_viruses):
        """Sets the found_viruses of this VirusScanAdvancedResult.

        Array of viruses found, if any  # noqa: E501

        :param found_viruses: The found_viruses of this VirusScanAdvancedResult.  # noqa: E501
        :type: list[VirusFound]
        """

        self._found_viruses = found_viruses

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
        if issubclass(VirusScanAdvancedResult, dict):
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
        if not isinstance(other, VirusScanAdvancedResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other