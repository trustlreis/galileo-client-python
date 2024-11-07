# openapi_client.CorporateCreditAndRTFApi

All URIs are relative to *https://api-sandbox.cv.gpsrv.com/intserv/4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_corporate_credit_change_history_post**](CorporateCreditAndRTFApi.md#get_corporate_credit_change_history_post) | **POST** /getCorporateCreditChangeHistory | Get Corporate Credit Change History
[**get_corporate_credit_summary_post**](CorporateCreditAndRTFApi.md#get_corporate_credit_summary_post) | **POST** /getCorporateCreditSummary | Get Corporate Credit Summary
[**is_corp_credit_funding_account_post**](CorporateCreditAndRTFApi.md#is_corp_credit_funding_account_post) | **POST** /isCorpCreditFundingAccount | Is Corporate Credit Funding Account
[**is_corp_credit_spending_account_post**](CorporateCreditAndRTFApi.md#is_corp_credit_spending_account_post) | **POST** /isCorpCreditSpendingAccount | Is Corporate Credit Spending Account
[**set_corporate_credit_limit_post**](CorporateCreditAndRTFApi.md#set_corporate_credit_limit_post) | **POST** /setCorporateCreditLimit | Set Corporate Credit Limit


# **get_corporate_credit_change_history_post**
> get_corporate_credit_change_history_post(response_content_type=response_content_type)

Get Corporate Credit Change History

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
    api_instance = openapi_client.CorporateCreditAndRTFApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Corporate Credit Change History
        api_instance.get_corporate_credit_change_history_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling CorporateCreditAndRTFApi->get_corporate_credit_change_history_post: %s\n" % e)
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

# **get_corporate_credit_summary_post**
> get_corporate_credit_summary_post(response_content_type=response_content_type)

Get Corporate Credit Summary

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
    api_instance = openapi_client.CorporateCreditAndRTFApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Corporate Credit Summary
        api_instance.get_corporate_credit_summary_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling CorporateCreditAndRTFApi->get_corporate_credit_summary_post: %s\n" % e)
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

# **is_corp_credit_funding_account_post**
> is_corp_credit_funding_account_post(response_content_type=response_content_type)

Is Corporate Credit Funding Account

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
    api_instance = openapi_client.CorporateCreditAndRTFApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Is Corporate Credit Funding Account
        api_instance.is_corp_credit_funding_account_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling CorporateCreditAndRTFApi->is_corp_credit_funding_account_post: %s\n" % e)
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

# **is_corp_credit_spending_account_post**
> is_corp_credit_spending_account_post(response_content_type=response_content_type)

Is Corporate Credit Spending Account

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
    api_instance = openapi_client.CorporateCreditAndRTFApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Is Corporate Credit Spending Account
        api_instance.is_corp_credit_spending_account_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling CorporateCreditAndRTFApi->is_corp_credit_spending_account_post: %s\n" % e)
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

# **set_corporate_credit_limit_post**
> set_corporate_credit_limit_post(response_content_type=response_content_type)

Set Corporate Credit Limit

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
    api_instance = openapi_client.CorporateCreditAndRTFApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Set Corporate Credit Limit
        api_instance.set_corporate_credit_limit_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling CorporateCreditAndRTFApi->set_corporate_credit_limit_post: %s\n" % e)
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

