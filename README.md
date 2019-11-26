# cloudmersive_virus_api_client
The Cloudmersive Virus Scan API lets you scan files and content for viruses and identify security issues with content.

This Python package provides a native API client for [Cloudmersive Anti-Virus Scan API](https://www.cloudmersive.com/virus-api)

- API version: v1
- Package version: 2.0.4
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import cloudmersive_virus_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cloudmersive_virus_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import cloudmersive_virus_api_client
from cloudmersive_virus_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_virus_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_virus_api_client.ScanApi(cloudmersive_virus_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

try:
    # Scan a file for viruses
    api_response = api_instance.scan_file(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->scan_file: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.cloudmersive.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ScanApi* | [**scan_file**](docs/ScanApi.md#scan_file) | **POST** /virus/scan/file | Scan a file for viruses
*ScanApi* | [**scan_file_advanced**](docs/ScanApi.md#scan_file_advanced) | **POST** /virus/scan/file/advanced | Advanced Scan a file for viruses
*ScanApi* | [**scan_website**](docs/ScanApi.md#scan_website) | **POST** /virus/scan/website | Scan a website for malicious content and threats


## Documentation For Models

 - [VirusFound](docs/VirusFound.md)
 - [VirusScanAdvancedResult](docs/VirusScanAdvancedResult.md)
 - [VirusScanResult](docs/VirusScanResult.md)
 - [WebsiteScanRequest](docs/WebsiteScanRequest.md)
 - [WebsiteScanResult](docs/WebsiteScanResult.md)


## Documentation For Authorization


## Apikey

- **Type**: API key
- **API key parameter name**: Apikey
- **Location**: HTTP header


## Author



