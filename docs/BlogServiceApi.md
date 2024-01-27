# swagger_client.BlogServiceApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_articles_get**](BlogServiceApi.md#api_v1_articles_get) | **GET** /api/v1/articles | 
[**api_v1_articles_post**](BlogServiceApi.md#api_v1_articles_post) | **POST** /api/v1/articles | 


# **api_v1_articles_get**
> ReturnAllArticles api_v1_articles_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlogServiceApi()

try:
    api_response = api_instance.api_v1_articles_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlogServiceApi->api_v1_articles_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ReturnAllArticles**](ReturnAllArticles.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_articles_post**
> Article api_v1_articles_post(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlogServiceApi()
body = swagger_client.CreateArticleRequest() # CreateArticleRequest | 

try:
    api_response = api_instance.api_v1_articles_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlogServiceApi->api_v1_articles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateArticleRequest**](CreateArticleRequest.md)|  | 

### Return type

[**Article**](Article.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

