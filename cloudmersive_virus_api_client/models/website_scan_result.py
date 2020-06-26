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


class WebsiteScanResult(object):
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
        'website_threat_type': 'str',
        'found_viruses': 'list[VirusFound]',
        'website_http_response_code': 'int'
    }

    attribute_map = {
        'clean_result': 'CleanResult',
        'website_threat_type': 'WebsiteThreatType',
        'found_viruses': 'FoundViruses',
        'website_http_response_code': 'WebsiteHttpResponseCode'
    }

    def __init__(self, clean_result=None, website_threat_type=None, found_viruses=None, website_http_response_code=None):  # noqa: E501
        """WebsiteScanResult - a model defined in Swagger"""  # noqa: E501

        self._clean_result = None
        self._website_threat_type = None
        self._found_viruses = None
        self._website_http_response_code = None
        self.discriminator = None

        if clean_result is not None:
            self.clean_result = clean_result
        if website_threat_type is not None:
            self.website_threat_type = website_threat_type
        if found_viruses is not None:
            self.found_viruses = found_viruses
        if website_http_response_code is not None:
            self.website_http_response_code = website_http_response_code

    @property
    def clean_result(self):
        """Gets the clean_result of this WebsiteScanResult.  # noqa: E501

        True if the scan contained no threats, false otherwise  # noqa: E501

        :return: The clean_result of this WebsiteScanResult.  # noqa: E501
        :rtype: bool
        """
        return self._clean_result

    @clean_result.setter
    def clean_result(self, clean_result):
        """Sets the clean_result of this WebsiteScanResult.

        True if the scan contained no threats, false otherwise  # noqa: E501

        :param clean_result: The clean_result of this WebsiteScanResult.  # noqa: E501
        :type: bool
        """

        self._clean_result = clean_result

    @property
    def website_threat_type(self):
        """Gets the website_threat_type of this WebsiteScanResult.  # noqa: E501

        Type of threat returned; can be None, Malware, ForcedDownload or Phishing  # noqa: E501

        :return: The website_threat_type of this WebsiteScanResult.  # noqa: E501
        :rtype: str
        """
        return self._website_threat_type

    @website_threat_type.setter
    def website_threat_type(self, website_threat_type):
        """Sets the website_threat_type of this WebsiteScanResult.

        Type of threat returned; can be None, Malware, ForcedDownload or Phishing  # noqa: E501

        :param website_threat_type: The website_threat_type of this WebsiteScanResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Malware", "Phishing", "ForcedDownload", "UnableToConnect"]  # noqa: E501
        if website_threat_type not in allowed_values:
            raise ValueError(
                "Invalid value for `website_threat_type` ({0}), must be one of {1}"  # noqa: E501
                .format(website_threat_type, allowed_values)
            )

        self._website_threat_type = website_threat_type

    @property
    def found_viruses(self):
        """Gets the found_viruses of this WebsiteScanResult.  # noqa: E501

        Array of viruses found, if any  # noqa: E501

        :return: The found_viruses of this WebsiteScanResult.  # noqa: E501
        :rtype: list[VirusFound]
        """
        return self._found_viruses

    @found_viruses.setter
    def found_viruses(self, found_viruses):
        """Sets the found_viruses of this WebsiteScanResult.

        Array of viruses found, if any  # noqa: E501

        :param found_viruses: The found_viruses of this WebsiteScanResult.  # noqa: E501
        :type: list[VirusFound]
        """

        self._found_viruses = found_viruses

    @property
    def website_http_response_code(self):
        """Gets the website_http_response_code of this WebsiteScanResult.  # noqa: E501

        The remote server URL HTTP reasponse code; useful for debugging issues with scanning; typically if the remote server returns a 200 or 300-series code this means a successful response, while a 400 or 500 series code would represent an error returned from the remote server for the provided URL.  # noqa: E501

        :return: The website_http_response_code of this WebsiteScanResult.  # noqa: E501
        :rtype: int
        """
        return self._website_http_response_code

    @website_http_response_code.setter
    def website_http_response_code(self, website_http_response_code):
        """Sets the website_http_response_code of this WebsiteScanResult.

        The remote server URL HTTP reasponse code; useful for debugging issues with scanning; typically if the remote server returns a 200 or 300-series code this means a successful response, while a 400 or 500 series code would represent an error returned from the remote server for the provided URL.  # noqa: E501

        :param website_http_response_code: The website_http_response_code of this WebsiteScanResult.  # noqa: E501
        :type: int
        """

        self._website_http_response_code = website_http_response_code

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
        if issubclass(WebsiteScanResult, dict):
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
        if not isinstance(other, WebsiteScanResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
