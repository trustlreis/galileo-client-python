# openapi_client.CreditApi

All URIs are relative to *https://api-sandbox.cv.gpsrv.com/intserv/4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_auto_pay_history_post**](CreditApi.md#get_auto_pay_history_post) | **POST** /getAutoPayHistory | Get Auto Pay History
[**get_credit_limit_change_history_post**](CreditApi.md#get_credit_limit_change_history_post) | **POST** /getCreditLimitChangeHistory | Get Credit Limit Change History
[**get_credit_summary_post**](CreditApi.md#get_credit_summary_post) | **POST** /getCreditSummary | Get Credit Summary
[**set_auto_pay_attempt_post**](CreditApi.md#set_auto_pay_attempt_post) | **POST** /setAutoPayAttempt | Set Auto Pay Attempt
[**set_auto_pay_plan_post**](CreditApi.md#set_auto_pay_plan_post) | **POST** /setAutoPayPlan | Set Auto Pay Plan
[**set_credit_limit_post**](CreditApi.md#set_credit_limit_post) | **POST** /setCreditLimit | Set Credit Limit


# **get_auto_pay_history_post**
> get_auto_pay_history_post(response_content_type=response_content_type)

Get Auto Pay History

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
    api_instance = openapi_client.CreditApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Auto Pay History
        api_instance.get_auto_pay_history_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling CreditApi->get_auto_pay_history_post: %s\n" % e)
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

# **get_credit_limit_change_history_post**
> get_credit_limit_change_history_post(response_content_type=response_content_type)

Get Credit Limit Change History

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
    api_instance = openapi_client.CreditApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Credit Limit Change History
        api_instance.get_credit_limit_change_history_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling CreditApi->get_credit_limit_change_history_post: %s\n" % e)
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

# **get_credit_summary_post**
> get_credit_summary_post(response_content_type=response_content_type)

Get Credit Summary

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
    api_instance = openapi_client.CreditApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Credit Summary
        api_instance.get_credit_summary_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling CreditApi->get_credit_summary_post: %s\n" % e)
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

# **set_auto_pay_attempt_post**
> set_auto_pay_attempt_post(response_content_type=response_content_type)

Set Auto Pay Attempt

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
    api_instance = openapi_client.CreditApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Set Auto Pay Attempt
        api_instance.set_auto_pay_attempt_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling CreditApi->set_auto_pay_attempt_post: %s\n" % e)
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

# **set_auto_pay_plan_post**
> set_auto_pay_plan_post(response_content_type=response_content_type)

Set Auto Pay Plan

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
    api_instance = openapi_client.CreditApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Set Auto Pay Plan
        api_instance.set_auto_pay_plan_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling CreditApi->set_auto_pay_plan_post: %s\n" % e)
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

# **set_credit_limit_post**
> set_credit_limit_post(response_content_type=response_content_type)

Set Credit Limit

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
    api_instance = openapi_client.CreditApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Set Credit Limit
        api_instance.set_credit_limit_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling CreditApi->set_credit_limit_post: %s\n" % e)
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

