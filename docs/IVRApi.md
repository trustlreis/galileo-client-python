# openapi_client.IVRApi

All URIs are relative to *https://api-sandbox.cv.gpsrv.com/intserv/4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ivr_call_post**](IVRApi.md#create_ivr_call_post) | **POST** /createIvrCall | Create IVR Call
[**get_ivr_call_identifier_post**](IVRApi.md#get_ivr_call_identifier_post) | **POST** /getIvrCallIdentifier | Get IVR Call Identifier
[**get_ivr_call_status_post**](IVRApi.md#get_ivr_call_status_post) | **POST** /getIvrCallStatus | Get IVR Call Status


# **create_ivr_call_post**
> create_ivr_call_post(response_content_type=response_content_type)

Create IVR Call

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
    api_instance = openapi_client.IVRApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Create IVR Call
        api_instance.create_ivr_call_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling IVRApi->create_ivr_call_post: %s\n" % e)
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

# **get_ivr_call_identifier_post**
> get_ivr_call_identifier_post(response_content_type=response_content_type)

Get IVR Call Identifier

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
    api_instance = openapi_client.IVRApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get IVR Call Identifier
        api_instance.get_ivr_call_identifier_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling IVRApi->get_ivr_call_identifier_post: %s\n" % e)
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

# **get_ivr_call_status_post**
> get_ivr_call_status_post(response_content_type=response_content_type)

Get IVR Call Status

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
    api_instance = openapi_client.IVRApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get IVR Call Status
        api_instance.get_ivr_call_status_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling IVRApi->get_ivr_call_status_post: %s\n" % e)
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

