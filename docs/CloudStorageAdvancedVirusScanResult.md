# CloudStorageAdvancedVirusScanResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | **bool** | True if the operation of retrieving the file, and scanning it were successfully completed, false if the file could not be downloaded from cloud storage, or if the file could not be scanned.  Note that successful completion does not mean the file is clean; for the output of the virus scanning operation itself, use the CleanResult and FoundViruses parameters. | [optional] 
**clean_result** | **bool** | True if the scan contained no viruses, false otherwise | [optional] 
**contains_executable** | **bool** | True if the scan contained an executable (application code), which can be a significant risk factor | [optional] 
**contains_invalid_file** | **bool** | True if the scan contained an invalid file (such as a PDF that is not a valid PDF, Word Document that is not a valid Word Document, etc.), which can be a significant risk factor | [optional] 
**contains_script** | **bool** | True if the scan contained a script (such as a PHP script, Python script, etc.) which can be a significant risk factor | [optional] 
**contains_password_protected_file** | **bool** | True if the scan contained a password protected or encrypted file, which can be a significant risk factor | [optional] 
**contains_restricted_file_format** | **bool** | True if the uploaded file is of a type that is not allowed based on the optional restrictFileTypes parameter, false otherwise; if restrictFileTypes is not set, this will always be false | [optional] 
**contains_macros** | **bool** | True if the uploaded file contains embedded Macros of other embedded threats within the document, which can be a significant risk factor | [optional] 
**verified_file_format** | **str** | For file format verification-supported file formats, the contents-verified file format of the file.  Null indicates that the file format is not supported for contents verification.  If a Virus or Malware is found, this field will always be set to Null. | [optional] 
**found_viruses** | [**list[CloudStorageVirusFound]**](CloudStorageVirusFound.md) | Array of viruses found, if any | [optional] 
**error_detailed_description** | **str** | Detailed error message if the operation was not successful | [optional] 
**file_size** | **int** | Size in bytes of the file that was retrieved and scanned | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


