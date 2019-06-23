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


class VirusFound(object):
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
        'file_name': 'str',
        'virus_name': 'str'
    }

    attribute_map = {
        'file_name': 'FileName',
        'virus_name': 'VirusName'
    }

    def __init__(self, file_name=None, virus_name=None):  # noqa: E501
        """VirusFound - a model defined in Swagger"""  # noqa: E501

        self._file_name = None
        self._virus_name = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if virus_name is not None:
            self.virus_name = virus_name

    @property
    def file_name(self):
        """Gets the file_name of this VirusFound.  # noqa: E501

        Name of the file containing the virus  # noqa: E501

        :return: The file_name of this VirusFound.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this VirusFound.

        Name of the file containing the virus  # noqa: E501

        :param file_name: The file_name of this VirusFound.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def virus_name(self):
        """Gets the virus_name of this VirusFound.  # noqa: E501

        Name of the virus that was found  # noqa: E501

        :return: The virus_name of this VirusFound.  # noqa: E501
        :rtype: str
        """
        return self._virus_name

    @virus_name.setter
    def virus_name(self, virus_name):
        """Sets the virus_name of this VirusFound.

        Name of the virus that was found  # noqa: E501

        :param virus_name: The virus_name of this VirusFound.  # noqa: E501
        :type: str
        """

        self._virus_name = virus_name

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
        if issubclass(VirusFound, dict):
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
        if not isinstance(other, VirusFound):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
