# openapi_client.AccountsAndCardsAccountAndCardBehaviorApi

All URIs are relative to *https://api-sandbox.cv.gpsrv.com/intserv/4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_features_post**](AccountsAndCardsAccountAndCardBehaviorApi.md#get_account_features_post) | **POST** /getAccountFeatures | Get Account Features
[**modify_status_post**](AccountsAndCardsAccountAndCardBehaviorApi.md#modify_status_post) | **POST** /modifyStatus | Modify Status
[**set_account_feature_post**](AccountsAndCardsAccountAndCardBehaviorApi.md#set_account_feature_post) | **POST** /setAccountFeature | Set Account Feature


# **get_account_features_post**
> get_account_features_post(response_content_type=response_content_type)

Get Account Features

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
    api_instance = openapi_client.AccountsAndCardsAccountAndCardBehaviorApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Account Features
        api_instance.get_account_features_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsAccountAndCardBehaviorApi->get_account_features_post: %s\n" % e)
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

# **modify_status_post**
> modify_status_post(response_content_type=response_content_type)

Modify Status

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
    api_instance = openapi_client.AccountsAndCardsAccountAndCardBehaviorApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Modify Status
        api_instance.modify_status_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsAccountAndCardBehaviorApi->modify_status_post: %s\n" % e)
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

# **set_account_feature_post**
> set_account_feature_post(response_content_type=response_content_type)

Set Account Feature

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
    api_instance = openapi_client.AccountsAndCardsAccountAndCardBehaviorApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Set Account Feature
        api_instance.set_account_feature_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsAccountAndCardBehaviorApi->set_account_feature_post: %s\n" % e)
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

