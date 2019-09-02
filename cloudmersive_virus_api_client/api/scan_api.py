# coding: utf-8

"""
    virusapi

    The Cloudmersive Virus Scan API lets you scan files and content for viruses and identify security issues with content.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cloudmersive_virus_api_client.api_client import ApiClient


class ScanApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def scan_file(self, input_file, **kwargs):  # noqa: E501
        """Scan a file for viruses  # noqa: E501

        Scan files and content for viruses. Leverage continuously updated signatures for millions of threats, and advanced high-performance scanning capabilities.  Over 5 million virus and malware signatures.  Continuous cloud-based updates.  Wide file format support including Office, PDF, HTML, Flash.  Zip support including .Zip, .Rar, .DMG, .Tar, and other archive formats.  Multi-threat scanning across viruses, malware, trojans, ransomware, and spyware.  High-speed in-memory scanning delivers subsecond typical response time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scan_file(input_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file input_file: Input file to perform the operation on. (required)
        :return: VirusScanResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.scan_file_with_http_info(input_file, **kwargs)  # noqa: E501
        else:
            (data) = self.scan_file_with_http_info(input_file, **kwargs)  # noqa: E501
            return data

    def scan_file_with_http_info(self, input_file, **kwargs):  # noqa: E501
        """Scan a file for viruses  # noqa: E501

        Scan files and content for viruses. Leverage continuously updated signatures for millions of threats, and advanced high-performance scanning capabilities.  Over 5 million virus and malware signatures.  Continuous cloud-based updates.  Wide file format support including Office, PDF, HTML, Flash.  Zip support including .Zip, .Rar, .DMG, .Tar, and other archive formats.  Multi-threat scanning across viruses, malware, trojans, ransomware, and spyware.  High-speed in-memory scanning delivers subsecond typical response time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scan_file_with_http_info(input_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file input_file: Input file to perform the operation on. (required)
        :return: VirusScanResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['input_file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scan_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'input_file' is set
        if ('input_file' not in params or
                params['input_file'] is None):
            raise ValueError("Missing the required parameter `input_file` when calling `scan_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'input_file' in params:
            local_var_files['inputFile'] = params['input_file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/virus/scan/file', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VirusScanResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def scan_website(self, input, **kwargs):  # noqa: E501
        """Scan a website for malicious content and threats  # noqa: E501

        Operation includes scanning the content of the URL for various types of malicious content and threats, including viruses and threats (including Phishing).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scan_website(input, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WebsiteScanRequest input: (required)
        :return: WebsiteScanResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.scan_website_with_http_info(input, **kwargs)  # noqa: E501
        else:
            (data) = self.scan_website_with_http_info(input, **kwargs)  # noqa: E501
            return data

    def scan_website_with_http_info(self, input, **kwargs):  # noqa: E501
        """Scan a website for malicious content and threats  # noqa: E501

        Operation includes scanning the content of the URL for various types of malicious content and threats, including viruses and threats (including Phishing).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scan_website_with_http_info(input, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WebsiteScanRequest input: (required)
        :return: WebsiteScanResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['input']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scan_website" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'input' is set
        if ('input' not in params or
                params['input'] is None):
            raise ValueError("Missing the required parameter `input` when calling `scan_website`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'input' in params:
            body_params = params['input']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/virus/scan/website', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WebsiteScanResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
