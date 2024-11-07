# openapi_client.TransactionsTransactionHistoryApi

All URIs are relative to *https://api-sandbox.cv.gpsrv.com/intserv/4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_overview_post**](TransactionsTransactionHistoryApi.md#get_account_overview_post) | **POST** /getAccountOverview | Get Account Overview
[**get_all_trans_history_post**](TransactionsTransactionHistoryApi.md#get_all_trans_history_post) | **POST** /getAllTransHistory | Get All Transaction History
[**get_trans_history_post**](TransactionsTransactionHistoryApi.md#get_trans_history_post) | **POST** /getTransHistory | Get Transaction History


# **get_account_overview_post**
> get_account_overview_post(response_content_type=response_content_type)

Get Account Overview

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
    api_instance = openapi_client.TransactionsTransactionHistoryApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Account Overview
        api_instance.get_account_overview_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsTransactionHistoryApi->get_account_overview_post: %s\n" % e)
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

# **get_all_trans_history_post**
> get_all_trans_history_post(response_content_type=response_content_type)

Get All Transaction History

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
    api_instance = openapi_client.TransactionsTransactionHistoryApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get All Transaction History
        api_instance.get_all_trans_history_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsTransactionHistoryApi->get_all_trans_history_post: %s\n" % e)
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

# **get_trans_history_post**
> get_trans_history_post(response_content_type=response_content_type)

Get Transaction History

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
    api_instance = openapi_client.TransactionsTransactionHistoryApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Transaction History
        api_instance.get_trans_history_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsTransactionHistoryApi->get_trans_history_post: %s\n" % e)
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

