# openapi_client.TransactionsAccountToAccountApi

All URIs are relative to *https://api-sandbox.cv.gpsrv.com/intserv/4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account_transfer_post**](TransactionsAccountToAccountApi.md#create_account_transfer_post) | **POST** /createAccountTransfer | Create Account Transfer
[**reverse_account_transfer_post**](TransactionsAccountToAccountApi.md#reverse_account_transfer_post) | **POST** /reverseAccountTransfer | Reverse Account Transfer


# **create_account_transfer_post**
> create_account_transfer_post(response_content_type=response_content_type)

Create Account Transfer

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-sandbox.cv.gpsrv.com/intserv/4.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api-sandbox.cv.gpsrv.com/intserv/4.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TransactionsAccountToAccountApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Create Account Transfer
        api_instance.create_account_transfer_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsAccountToAccountApi->create_account_transfer_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reverse_account_transfer_post**
> reverse_account_transfer_post(response_content_type=response_content_type)

Reverse Account Transfer

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-sandbox.cv.gpsrv.com/intserv/4.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api-sandbox.cv.gpsrv.com/intserv/4.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TransactionsAccountToAccountApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Reverse Account Transfer
        api_instance.reverse_account_transfer_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsAccountToAccountApi->reverse_account_transfer_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

