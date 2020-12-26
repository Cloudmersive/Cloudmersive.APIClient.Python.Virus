# CloudStorageVirusScanResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | **bool** | True if the operation of retrieving the file, and scanning it were successfully completed, false if the file could not be downloaded from cloud storage, or if the file could not be scanned.  Note that successful completion does not mean the file is clean; for the output of the virus scanning operation itself, use the CleanResult and FoundViruses parameters. | [optional] 
**clean_result** | **bool** | True if the scan contained no viruses, false otherwise | [optional] 
**found_viruses** | [**list[CloudStorageVirusFound]**](CloudStorageVirusFound.md) | Array of viruses found, if any | [optional] 
**error_detailed_description** | **str** | Detailed error message if the operation was not successful | [optional] 
**file_size** | **int** | Size in bytes of the file that was retrieved and scanned | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


