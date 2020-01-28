# WebsiteScanResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clean_result** | **bool** | True if the scan contained no threats, false otherwise | [optional] 
**website_threat_type** | **str** | Type of threat returned; can be None, Malware, ForcedDownload or Phishing | [optional] 
**found_viruses** | [**list[VirusFound]**](VirusFound.md) | Array of viruses found, if any | [optional] 
**website_http_response_code** | **int** | The remote server URL HTTP reasponse code; useful for debugging issues with scanning; typically if the remote server returns a 200 or 300-series code this means a successful response, while a 400 or 500 series code would represent an error returned from the remote server for the provided URL. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


