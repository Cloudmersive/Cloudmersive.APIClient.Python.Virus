# cloudmersive_virus_api_client.ScanCloudStorageApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scan_cloud_storage_scan_aws_s3_file**](ScanCloudStorageApi.md#scan_cloud_storage_scan_aws_s3_file) | **POST** /virus/scan/cloud-storage/aws-s3/single | Scan an AWS S3 file for viruses
[**scan_cloud_storage_scan_aws_s3_file_advanced**](ScanCloudStorageApi.md#scan_cloud_storage_scan_aws_s3_file_advanced) | **POST** /virus/scan/cloud-storage/aws-s3/single/advanced | Advanced Scan an AWS S3 file for viruses
[**scan_cloud_storage_scan_azure_blob**](ScanCloudStorageApi.md#scan_cloud_storage_scan_azure_blob) | **POST** /virus/scan/cloud-storage/azure-blob/single | Scan an Azure Blob for viruses
[**scan_cloud_storage_scan_azure_blob_advanced**](ScanCloudStorageApi.md#scan_cloud_storage_scan_azure_blob_advanced) | **POST** /virus/scan/cloud-storage/azure-blob/single/advanced | Advanced Scan an Azure Blob for viruses
[**scan_cloud_storage_scan_gcp_storage_file**](ScanCloudStorageApi.md#scan_cloud_storage_scan_gcp_storage_file) | **POST** /virus/scan/cloud-storage/gcp-storage/single | Scan an Google Cloud Platform (GCP) Storage file for viruses
[**scan_cloud_storage_scan_gcp_storage_file_advanced**](ScanCloudStorageApi.md#scan_cloud_storage_scan_gcp_storage_file_advanced) | **POST** /virus/scan/cloud-storage/gcp-storage/single/advanced | Advanced Scan an Google Cloud Platform (GCP) Storage file for viruses


# **scan_cloud_storage_scan_aws_s3_file**
> CloudStorageVirusScanResult scan_cloud_storage_scan_aws_s3_file(access_key, secret_key, bucket_region, bucket_name, key_name)

Scan an AWS S3 file for viruses

Scan the contents of a single AWS S3 file and its content for viruses. Leverage continuously updated signatures for millions of threats, and advanced high-performance scanning capabilities.  Over 17 million virus and malware signatures.  Continuous cloud-based updates.  Wide file format support including Office, PDF, HTML, Flash.  Zip support including .Zip, .Rar, .DMG, .Tar, and other archive formats.  Multi-threat scanning across viruses, malware, trojans, ransomware, and spyware.  High-speed in-memory scanning delivers subsecond typical response time.

### Example
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
api_instance = cloudmersive_virus_api_client.ScanCloudStorageApi(cloudmersive_virus_api_client.ApiClient(configuration))
access_key = 'access_key_example' # str | AWS S3 access key for the S3 bucket; you can get this from My Security Credentials in the AWS console
secret_key = 'secret_key_example' # str | AWS S3 secret key for the S3 bucket; you can get this from My Security Credentials in the AWS console
bucket_region = 'bucket_region_example' # str | Name of the region of the S3 bucket, such as 'US-East-1'
bucket_name = 'bucket_name_example' # str | Name of the S3 bucket
key_name = 'key_name_example' # str | Key name (also called file name) of the file in S3 that you wish to scan for viruses

try:
    # Scan an AWS S3 file for viruses
    api_response = api_instance.scan_cloud_storage_scan_aws_s3_file(access_key, secret_key, bucket_region, bucket_name, key_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanCloudStorageApi->scan_cloud_storage_scan_aws_s3_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_key** | **str**| AWS S3 access key for the S3 bucket; you can get this from My Security Credentials in the AWS console | 
 **secret_key** | **str**| AWS S3 secret key for the S3 bucket; you can get this from My Security Credentials in the AWS console | 
 **bucket_region** | **str**| Name of the region of the S3 bucket, such as &#39;US-East-1&#39; | 
 **bucket_name** | **str**| Name of the S3 bucket | 
 **key_name** | **str**| Key name (also called file name) of the file in S3 that you wish to scan for viruses | 

### Return type

[**CloudStorageVirusScanResult**](CloudStorageVirusScanResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_cloud_storage_scan_aws_s3_file_advanced**
> CloudStorageAdvancedVirusScanResult scan_cloud_storage_scan_aws_s3_file_advanced(access_key, secret_key, bucket_region, bucket_name, key_name, allow_executables=allow_executables, allow_invalid_files=allow_invalid_files, allow_scripts=allow_scripts, allow_password_protected_files=allow_password_protected_files, allow_macros=allow_macros, restrict_file_types=restrict_file_types)

Advanced Scan an AWS S3 file for viruses

Advanced Scan the contents of a single AWS S3 file and its content for viruses and threats. Advanced Scan files with 360-degree Content Protection across Viruses and Malware, executables, invalid files, scripts, and even restrictions on accepted file types with complete content verification. Customize threat rules to your needs. Leverage continuously updated signatures for millions of threats, and advanced high-performance scanning capabilities.  Over 17 million virus and malware signatures.  Continuous cloud-based updates.  Block threats beyond viruses including executables, scripts, invalid files, and more.  Optionally limit input files to a specific set of file types (e.g. PDF and Word Documents only).  Wide file format support including Office, PDF, HTML, Flash.  Zip support including .Zip, .Rar, .DMG, .Tar, and other archive formats.  Multi-threat scanning across viruses, malware, trojans, ransomware, and spyware.  High-speed in-memory scanning delivers subsecond typical response time.

### Example
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
api_instance = cloudmersive_virus_api_client.ScanCloudStorageApi(cloudmersive_virus_api_client.ApiClient(configuration))
access_key = 'access_key_example' # str | AWS S3 access key for the S3 bucket; you can get this from My Security Credentials in the AWS console
secret_key = 'secret_key_example' # str | AWS S3 secret key for the S3 bucket; you can get this from My Security Credentials in the AWS console
bucket_region = 'bucket_region_example' # str | Name of the region of the S3 bucket, such as 'US-East-1'
bucket_name = 'bucket_name_example' # str | Name of the S3 bucket
key_name = 'key_name_example' # str | Key name (also called file name) of the file in S3 that you wish to scan for viruses
allow_executables = true # bool | Set to false to block executable files (program code) from being allowed in the input file.  Default is false (recommended). (optional)
allow_invalid_files = true # bool | Set to false to block invalid files, such as a PDF file that is not really a valid PDF file, or a Word Document that is not a valid Word Document.  Default is false (recommended). (optional)
allow_scripts = true # bool | Set to false to block script files, such as a PHP files, Python scripts, and other malicious content or security threats that can be embedded in the file.  Set to true to allow these file types.  Default is false (recommended). (optional)
allow_password_protected_files = true # bool | Set to false to block password protected and encrypted files, such as encrypted zip and rar files, and other files that seek to circumvent scanning through passwords.  Set to true to allow these file types.  Default is false (recommended). (optional)
allow_macros = true # bool | Set to false to block macros and other threats embedded in document files, such as Word, Excel and PowerPoint embedded Macros, and other files that contain embedded content threats.  Set to true to allow these file types.  Default is false (recommended). (optional)
restrict_file_types = 'restrict_file_types_example' # str | Specify a restricted set of file formats to allow as clean as a comma-separated list of file formats, such as .pdf,.docx,.png would allow only PDF, PNG and Word document files.  All files must pass content verification against this list of file formats, if they do not, then the result will be returned as CleanResult=false.  Set restrictFileTypes parameter to null or empty string to disable; default is disabled. (optional)

try:
    # Advanced Scan an AWS S3 file for viruses
    api_response = api_instance.scan_cloud_storage_scan_aws_s3_file_advanced(access_key, secret_key, bucket_region, bucket_name, key_name, allow_executables=allow_executables, allow_invalid_files=allow_invalid_files, allow_scripts=allow_scripts, allow_password_protected_files=allow_password_protected_files, allow_macros=allow_macros, restrict_file_types=restrict_file_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanCloudStorageApi->scan_cloud_storage_scan_aws_s3_file_advanced: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_key** | **str**| AWS S3 access key for the S3 bucket; you can get this from My Security Credentials in the AWS console | 
 **secret_key** | **str**| AWS S3 secret key for the S3 bucket; you can get this from My Security Credentials in the AWS console | 
 **bucket_region** | **str**| Name of the region of the S3 bucket, such as &#39;US-East-1&#39; | 
 **bucket_name** | **str**| Name of the S3 bucket | 
 **key_name** | **str**| Key name (also called file name) of the file in S3 that you wish to scan for viruses | 
 **allow_executables** | **bool**| Set to false to block executable files (program code) from being allowed in the input file.  Default is false (recommended). | [optional] 
 **allow_invalid_files** | **bool**| Set to false to block invalid files, such as a PDF file that is not really a valid PDF file, or a Word Document that is not a valid Word Document.  Default is false (recommended). | [optional] 
 **allow_scripts** | **bool**| Set to false to block script files, such as a PHP files, Python scripts, and other malicious content or security threats that can be embedded in the file.  Set to true to allow these file types.  Default is false (recommended). | [optional] 
 **allow_password_protected_files** | **bool**| Set to false to block password protected and encrypted files, such as encrypted zip and rar files, and other files that seek to circumvent scanning through passwords.  Set to true to allow these file types.  Default is false (recommended). | [optional] 
 **allow_macros** | **bool**| Set to false to block macros and other threats embedded in document files, such as Word, Excel and PowerPoint embedded Macros, and other files that contain embedded content threats.  Set to true to allow these file types.  Default is false (recommended). | [optional] 
 **restrict_file_types** | **str**| Specify a restricted set of file formats to allow as clean as a comma-separated list of file formats, such as .pdf,.docx,.png would allow only PDF, PNG and Word document files.  All files must pass content verification against this list of file formats, if they do not, then the result will be returned as CleanResult&#x3D;false.  Set restrictFileTypes parameter to null or empty string to disable; default is disabled. | [optional] 

### Return type

[**CloudStorageAdvancedVirusScanResult**](CloudStorageAdvancedVirusScanResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_cloud_storage_scan_azure_blob**
> CloudStorageVirusScanResult scan_cloud_storage_scan_azure_blob(connection_string, container_name, blob_path)

Scan an Azure Blob for viruses

Scan the contents of a single Azure Blob and its content for viruses. Leverage continuously updated signatures for millions of threats, and advanced high-performance scanning capabilities.  Over 17 million virus and malware signatures.  Continuous cloud-based updates.  Wide file format support including Office, PDF, HTML, Flash.  Zip support including .Zip, .Rar, .DMG, .Tar, and other archive formats.  Multi-threat scanning across viruses, malware, trojans, ransomware, and spyware.  High-speed in-memory scanning delivers subsecond typical response time.

### Example
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
api_instance = cloudmersive_virus_api_client.ScanCloudStorageApi(cloudmersive_virus_api_client.ApiClient(configuration))
connection_string = 'connection_string_example' # str | Connection string for the Azure Blob Storage Account; you can get this connection string from the Access Keys tab of the Storage Account blade in the Azure Portal.
container_name = 'container_name_example' # str | Name of the Blob container within the Azure Blob Storage account
blob_path = 'blob_path_example' # str | Path to the blob within the container, such as 'hello.pdf' or '/folder/subfolder/world.pdf'

try:
    # Scan an Azure Blob for viruses
    api_response = api_instance.scan_cloud_storage_scan_azure_blob(connection_string, container_name, blob_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanCloudStorageApi->scan_cloud_storage_scan_azure_blob: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_string** | **str**| Connection string for the Azure Blob Storage Account; you can get this connection string from the Access Keys tab of the Storage Account blade in the Azure Portal. | 
 **container_name** | **str**| Name of the Blob container within the Azure Blob Storage account | 
 **blob_path** | **str**| Path to the blob within the container, such as &#39;hello.pdf&#39; or &#39;/folder/subfolder/world.pdf&#39; | 

### Return type

[**CloudStorageVirusScanResult**](CloudStorageVirusScanResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_cloud_storage_scan_azure_blob_advanced**
> CloudStorageAdvancedVirusScanResult scan_cloud_storage_scan_azure_blob_advanced(connection_string, container_name, blob_path, allow_executables=allow_executables, allow_invalid_files=allow_invalid_files, allow_scripts=allow_scripts, allow_password_protected_files=allow_password_protected_files, allow_macros=allow_macros, restrict_file_types=restrict_file_types)

Advanced Scan an Azure Blob for viruses

Advanced Scan the contents of a single Azure Blob and its content for viruses and threats.  Advanced Scan files with 360-degree Content Protection across Viruses and Malware, executables, invalid files, scripts, and even restrictions on accepted file types with complete content verification. Customize threat rules to your needs. Leverage continuously updated signatures for millions of threats, and advanced high-performance scanning capabilities.  Over 17 million virus and malware signatures.  Continuous cloud-based updates.  Block threats beyond viruses including executables, scripts, invalid files, and more.  Optionally limit input files to a specific set of file types (e.g. PDF and Word Documents only).  Wide file format support including Office, PDF, HTML, Flash.  Zip support including .Zip, .Rar, .DMG, .Tar, and other archive formats.  Multi-threat scanning across viruses, malware, trojans, ransomware, and spyware.  High-speed in-memory scanning delivers subsecond typical response time.

### Example
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
api_instance = cloudmersive_virus_api_client.ScanCloudStorageApi(cloudmersive_virus_api_client.ApiClient(configuration))
connection_string = 'connection_string_example' # str | Connection string for the Azure Blob Storage Account; you can get this connection string from the Access Keys tab of the Storage Account blade in the Azure Portal.
container_name = 'container_name_example' # str | Name of the Blob container within the Azure Blob Storage account
blob_path = 'blob_path_example' # str | Path to the blob within the container, such as 'hello.pdf' or '/folder/subfolder/world.pdf'
allow_executables = true # bool | Set to false to block executable files (program code) from being allowed in the input file.  Default is false (recommended). (optional)
allow_invalid_files = true # bool | Set to false to block invalid files, such as a PDF file that is not really a valid PDF file, or a Word Document that is not a valid Word Document.  Default is false (recommended). (optional)
allow_scripts = true # bool | Set to false to block script files, such as a PHP files, Python scripts, and other malicious content or security threats that can be embedded in the file.  Set to true to allow these file types.  Default is false (recommended). (optional)
allow_password_protected_files = true # bool | Set to false to block password protected and encrypted files, such as encrypted zip and rar files, and other files that seek to circumvent scanning through passwords.  Set to true to allow these file types.  Default is false (recommended). (optional)
allow_macros = true # bool | Set to false to block macros and other threats embedded in document files, such as Word, Excel and PowerPoint embedded Macros, and other files that contain embedded content threats.  Set to true to allow these file types.  Default is false (recommended). (optional)
restrict_file_types = 'restrict_file_types_example' # str | Specify a restricted set of file formats to allow as clean as a comma-separated list of file formats, such as .pdf,.docx,.png would allow only PDF, PNG and Word document files.  All files must pass content verification against this list of file formats, if they do not, then the result will be returned as CleanResult=false.  Set restrictFileTypes parameter to null or empty string to disable; default is disabled. (optional)

try:
    # Advanced Scan an Azure Blob for viruses
    api_response = api_instance.scan_cloud_storage_scan_azure_blob_advanced(connection_string, container_name, blob_path, allow_executables=allow_executables, allow_invalid_files=allow_invalid_files, allow_scripts=allow_scripts, allow_password_protected_files=allow_password_protected_files, allow_macros=allow_macros, restrict_file_types=restrict_file_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanCloudStorageApi->scan_cloud_storage_scan_azure_blob_advanced: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_string** | **str**| Connection string for the Azure Blob Storage Account; you can get this connection string from the Access Keys tab of the Storage Account blade in the Azure Portal. | 
 **container_name** | **str**| Name of the Blob container within the Azure Blob Storage account | 
 **blob_path** | **str**| Path to the blob within the container, such as &#39;hello.pdf&#39; or &#39;/folder/subfolder/world.pdf&#39; | 
 **allow_executables** | **bool**| Set to false to block executable files (program code) from being allowed in the input file.  Default is false (recommended). | [optional] 
 **allow_invalid_files** | **bool**| Set to false to block invalid files, such as a PDF file that is not really a valid PDF file, or a Word Document that is not a valid Word Document.  Default is false (recommended). | [optional] 
 **allow_scripts** | **bool**| Set to false to block script files, such as a PHP files, Python scripts, and other malicious content or security threats that can be embedded in the file.  Set to true to allow these file types.  Default is false (recommended). | [optional] 
 **allow_password_protected_files** | **bool**| Set to false to block password protected and encrypted files, such as encrypted zip and rar files, and other files that seek to circumvent scanning through passwords.  Set to true to allow these file types.  Default is false (recommended). | [optional] 
 **allow_macros** | **bool**| Set to false to block macros and other threats embedded in document files, such as Word, Excel and PowerPoint embedded Macros, and other files that contain embedded content threats.  Set to true to allow these file types.  Default is false (recommended). | [optional] 
 **restrict_file_types** | **str**| Specify a restricted set of file formats to allow as clean as a comma-separated list of file formats, such as .pdf,.docx,.png would allow only PDF, PNG and Word document files.  All files must pass content verification against this list of file formats, if they do not, then the result will be returned as CleanResult&#x3D;false.  Set restrictFileTypes parameter to null or empty string to disable; default is disabled. | [optional] 

### Return type

[**CloudStorageAdvancedVirusScanResult**](CloudStorageAdvancedVirusScanResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_cloud_storage_scan_gcp_storage_file**
> CloudStorageVirusScanResult scan_cloud_storage_scan_gcp_storage_file(bucket_name, object_name, json_credential_file)

Scan an Google Cloud Platform (GCP) Storage file for viruses

Scan the contents of a single Google Cloud Platform (GCP) Storage file and its content for viruses. Leverage continuously updated signatures for millions of threats, and advanced high-performance scanning capabilities.  Over 17 million virus and malware signatures.  Continuous cloud-based updates.  Wide file format support including Office, PDF, HTML, Flash.  Zip support including .Zip, .Rar, .DMG, .Tar, and other archive formats.  Multi-threat scanning across viruses, malware, trojans, ransomware, and spyware.  High-speed in-memory scanning delivers subsecond typical response time.

### Example
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
api_instance = cloudmersive_virus_api_client.ScanCloudStorageApi(cloudmersive_virus_api_client.ApiClient(configuration))
bucket_name = 'bucket_name_example' # str | Name of the bucket in Google Cloud Storage
object_name = 'object_name_example' # str | Name of the object or file in Google Cloud Storage
json_credential_file = '/path/to/file.txt' # file | Service Account credential for Google Cloud stored in a JSON file.

try:
    # Scan an Google Cloud Platform (GCP) Storage file for viruses
    api_response = api_instance.scan_cloud_storage_scan_gcp_storage_file(bucket_name, object_name, json_credential_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanCloudStorageApi->scan_cloud_storage_scan_gcp_storage_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_name** | **str**| Name of the bucket in Google Cloud Storage | 
 **object_name** | **str**| Name of the object or file in Google Cloud Storage | 
 **json_credential_file** | **file**| Service Account credential for Google Cloud stored in a JSON file. | 

### Return type

[**CloudStorageVirusScanResult**](CloudStorageVirusScanResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_cloud_storage_scan_gcp_storage_file_advanced**
> CloudStorageAdvancedVirusScanResult scan_cloud_storage_scan_gcp_storage_file_advanced(bucket_name, object_name, json_credential_file, allow_executables=allow_executables, allow_invalid_files=allow_invalid_files, allow_scripts=allow_scripts, allow_password_protected_files=allow_password_protected_files, allow_macros=allow_macros, restrict_file_types=restrict_file_types)

Advanced Scan an Google Cloud Platform (GCP) Storage file for viruses

Advanced Scan the contents of a single Google Cloud Platform (GCP) Storage file and its content for viruses and threats. Advanced Scan files with 360-degree Content Protection across Viruses and Malware, executables, invalid files, scripts, and even restrictions on accepted file types with complete content verification. Customize threat rules to your needs. Leverage continuously updated signatures for millions of threats, and advanced high-performance scanning capabilities.  Over 17 million virus and malware signatures.  Continuous cloud-based updates.  Block threats beyond viruses including executables, scripts, invalid files, and more.  Optionally limit input files to a specific set of file types (e.g. PDF and Word Documents only).  Wide file format support including Office, PDF, HTML, Flash.  Zip support including .Zip, .Rar, .DMG, .Tar, and other archive formats.  Multi-threat scanning across viruses, malware, trojans, ransomware, and spyware.  High-speed in-memory scanning delivers subsecond typical response time.

### Example
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
api_instance = cloudmersive_virus_api_client.ScanCloudStorageApi(cloudmersive_virus_api_client.ApiClient(configuration))
bucket_name = 'bucket_name_example' # str | Name of the bucket in Google Cloud Storage
object_name = 'object_name_example' # str | Name of the object or file in Google Cloud Storage
json_credential_file = '/path/to/file.txt' # file | Service Account credential for Google Cloud stored in a JSON file.
allow_executables = true # bool | Set to false to block executable files (program code) from being allowed in the input file.  Default is false (recommended). (optional)
allow_invalid_files = true # bool | Set to false to block invalid files, such as a PDF file that is not really a valid PDF file, or a Word Document that is not a valid Word Document.  Default is false (recommended). (optional)
allow_scripts = true # bool | Set to false to block script files, such as a PHP files, Python scripts, and other malicious content or security threats that can be embedded in the file.  Set to true to allow these file types.  Default is false (recommended). (optional)
allow_password_protected_files = true # bool | Set to false to block password protected and encrypted files, such as encrypted zip and rar files, and other files that seek to circumvent scanning through passwords.  Set to true to allow these file types.  Default is false (recommended). (optional)
allow_macros = true # bool | Set to false to block macros and other threats embedded in document files, such as Word, Excel and PowerPoint embedded Macros, and other files that contain embedded content threats.  Set to true to allow these file types.  Default is false (recommended). (optional)
restrict_file_types = 'restrict_file_types_example' # str | Specify a restricted set of file formats to allow as clean as a comma-separated list of file formats, such as .pdf,.docx,.png would allow only PDF, PNG and Word document files.  All files must pass content verification against this list of file formats, if they do not, then the result will be returned as CleanResult=false.  Set restrictFileTypes parameter to null or empty string to disable; default is disabled. (optional)

try:
    # Advanced Scan an Google Cloud Platform (GCP) Storage file for viruses
    api_response = api_instance.scan_cloud_storage_scan_gcp_storage_file_advanced(bucket_name, object_name, json_credential_file, allow_executables=allow_executables, allow_invalid_files=allow_invalid_files, allow_scripts=allow_scripts, allow_password_protected_files=allow_password_protected_files, allow_macros=allow_macros, restrict_file_types=restrict_file_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanCloudStorageApi->scan_cloud_storage_scan_gcp_storage_file_advanced: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_name** | **str**| Name of the bucket in Google Cloud Storage | 
 **object_name** | **str**| Name of the object or file in Google Cloud Storage | 
 **json_credential_file** | **file**| Service Account credential for Google Cloud stored in a JSON file. | 
 **allow_executables** | **bool**| Set to false to block executable files (program code) from being allowed in the input file.  Default is false (recommended). | [optional] 
 **allow_invalid_files** | **bool**| Set to false to block invalid files, such as a PDF file that is not really a valid PDF file, or a Word Document that is not a valid Word Document.  Default is false (recommended). | [optional] 
 **allow_scripts** | **bool**| Set to false to block script files, such as a PHP files, Python scripts, and other malicious content or security threats that can be embedded in the file.  Set to true to allow these file types.  Default is false (recommended). | [optional] 
 **allow_password_protected_files** | **bool**| Set to false to block password protected and encrypted files, such as encrypted zip and rar files, and other files that seek to circumvent scanning through passwords.  Set to true to allow these file types.  Default is false (recommended). | [optional] 
 **allow_macros** | **bool**| Set to false to block macros and other threats embedded in document files, such as Word, Excel and PowerPoint embedded Macros, and other files that contain embedded content threats.  Set to true to allow these file types.  Default is false (recommended). | [optional] 
 **restrict_file_types** | **str**| Specify a restricted set of file formats to allow as clean as a comma-separated list of file formats, such as .pdf,.docx,.png would allow only PDF, PNG and Word document files.  All files must pass content verification against this list of file formats, if they do not, then the result will be returned as CleanResult&#x3D;false.  Set restrictFileTypes parameter to null or empty string to disable; default is disabled. | [optional] 

### Return type

[**CloudStorageAdvancedVirusScanResult**](CloudStorageAdvancedVirusScanResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

