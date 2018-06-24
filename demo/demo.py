from __future__ import print_function
import time
import cloudmersive_virus_api_client
from cloudmersive_virus_api_client.rest import ApiException
from pprint import pprint










# create an instance of the API class
api_instance = cloudmersive_virus_api_client.ScanApi()
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.

api_instance.api_client.configuration.api_key = {}
api_instance.api_client.configuration.api_key['Apikey'] = '04d1a7be-c9d1-4d93-8ec4-e7545c2a570a'

try:
    # Scan a file for viruses
    api_response = api_instance.scan_file(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->scan_file: %s\n" % e)