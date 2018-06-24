from __future__ import print_function
import time
import cloudmersive_barcode_api_client
from cloudmersive_barcode_api_client.rest import ApiException
from pprint import pprint








# create an instance of the API class
api_instance = cloudmersive_barcode_api_client.BarcodeLookupApi()
value = 'value_example' # str | Barcode value

api_instance.api_client.configuration.api_key = {}
api_instance.api_client.configuration.api_key['Apikey'] = '04d1a7be-c9d1-4d93-8ec4-e7545c2a570a'

try:
    # Lookup a barcode value and return product data
    api_response = api_instance.barcode_lookup_ean_lookup(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BarcodeLookupApi->barcode_lookup_ean_lookup: %s\n" % e)