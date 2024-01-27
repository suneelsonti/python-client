import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlogServiceApi(swagger_client.ApiClient())

try:
    api_response = api_instance.api_v1_articles_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlogServiceApi->api_v1_articles_get: %s\n" % e)