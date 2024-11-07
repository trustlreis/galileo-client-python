# openapi_client.AccountsAndCardsCustomerNotesApi

All URIs are relative to *https://api-sandbox.cv.gpsrv.com/intserv/4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_customer_note_post**](AccountsAndCardsCustomerNotesApi.md#add_customer_note_post) | **POST** /addCustomerNote | Add Customer Note
[**get_customer_note_history_post**](AccountsAndCardsCustomerNotesApi.md#get_customer_note_history_post) | **POST** /getCustomerNoteHistory | Get Customer Note History


# **add_customer_note_post**
> add_customer_note_post(response_content_type=response_content_type)

Add Customer Note

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
    api_instance = openapi_client.AccountsAndCardsCustomerNotesApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Add Customer Note
        api_instance.add_customer_note_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsCustomerNotesApi->add_customer_note_post: %s\n" % e)
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

# **get_customer_note_history_post**
> get_customer_note_history_post(response_content_type=response_content_type)

Get Customer Note History

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
    api_instance = openapi_client.AccountsAndCardsCustomerNotesApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Customer Note History
        api_instance.get_customer_note_history_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsCustomerNotesApi->get_customer_note_history_post: %s\n" % e)
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

