# openapi_client.AccountLevelControlsApi

All URIs are relative to *https://api-sandbox.cv.gpsrv.com/intserv/4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_account_level_auth_control_post**](AccountLevelControlsApi.md#delete_account_level_auth_control_post) | **POST** /deleteAccountLevelAuthControl | Delete Account Level Auth Control
[**delete_account_level_mcc_control_post**](AccountLevelControlsApi.md#delete_account_level_mcc_control_post) | **POST** /deleteAccountLevelMccControl | Delete Account Level MCC Control
[**delete_account_level_merchant_control_post**](AccountLevelControlsApi.md#delete_account_level_merchant_control_post) | **POST** /deleteAccountLevelMerchantControl | Delete Account Level Merchant Control
[**get_auth_control_post**](AccountLevelControlsApi.md#get_auth_control_post) | **POST** /getAuthControl | Get Auth Control
[**get_mcc_controls_post**](AccountLevelControlsApi.md#get_mcc_controls_post) | **POST** /getMccControls | Get MCC Controls
[**get_merchant_controls_post**](AccountLevelControlsApi.md#get_merchant_controls_post) | **POST** /getMerchantControls | Get Merchant Controls
[**set_account_level_auth_control_post**](AccountLevelControlsApi.md#set_account_level_auth_control_post) | **POST** /setAccountLevelAuthControl | Set Account-Level Auth Control 
[**set_account_level_mcc_control_post**](AccountLevelControlsApi.md#set_account_level_mcc_control_post) | **POST** /setAccountLevelMccControl | Set Account-Level MCC Control
[**set_account_level_merchant_control_post**](AccountLevelControlsApi.md#set_account_level_merchant_control_post) | **POST** /setAccountLevelMerchantControl | Set Account-Level Merchant Control


# **delete_account_level_auth_control_post**
> delete_account_level_auth_control_post(response_content_type=response_content_type)

Delete Account Level Auth Control

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
    api_instance = openapi_client.AccountLevelControlsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Delete Account Level Auth Control
        api_instance.delete_account_level_auth_control_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountLevelControlsApi->delete_account_level_auth_control_post: %s\n" % e)
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

# **delete_account_level_mcc_control_post**
> delete_account_level_mcc_control_post(response_content_type=response_content_type)

Delete Account Level MCC Control

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
    api_instance = openapi_client.AccountLevelControlsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Delete Account Level MCC Control
        api_instance.delete_account_level_mcc_control_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountLevelControlsApi->delete_account_level_mcc_control_post: %s\n" % e)
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

# **delete_account_level_merchant_control_post**
> delete_account_level_merchant_control_post(response_content_type=response_content_type)

Delete Account Level Merchant Control

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
    api_instance = openapi_client.AccountLevelControlsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Delete Account Level Merchant Control
        api_instance.delete_account_level_merchant_control_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountLevelControlsApi->delete_account_level_merchant_control_post: %s\n" % e)
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

# **get_auth_control_post**
> get_auth_control_post(response_content_type=response_content_type)

Get Auth Control

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
    api_instance = openapi_client.AccountLevelControlsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Auth Control
        api_instance.get_auth_control_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountLevelControlsApi->get_auth_control_post: %s\n" % e)
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

# **get_mcc_controls_post**
> get_mcc_controls_post(response_content_type=response_content_type)

Get MCC Controls

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
    api_instance = openapi_client.AccountLevelControlsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get MCC Controls
        api_instance.get_mcc_controls_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountLevelControlsApi->get_mcc_controls_post: %s\n" % e)
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

# **get_merchant_controls_post**
> get_merchant_controls_post(response_content_type=response_content_type)

Get Merchant Controls

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
    api_instance = openapi_client.AccountLevelControlsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Merchant Controls
        api_instance.get_merchant_controls_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountLevelControlsApi->get_merchant_controls_post: %s\n" % e)
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

# **set_account_level_auth_control_post**
> set_account_level_auth_control_post(response_content_type=response_content_type)

Set Account-Level Auth Control 

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
    api_instance = openapi_client.AccountLevelControlsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Set Account-Level Auth Control 
        api_instance.set_account_level_auth_control_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountLevelControlsApi->set_account_level_auth_control_post: %s\n" % e)
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

# **set_account_level_mcc_control_post**
> set_account_level_mcc_control_post(response_content_type=response_content_type)

Set Account-Level MCC Control

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
    api_instance = openapi_client.AccountLevelControlsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Set Account-Level MCC Control
        api_instance.set_account_level_mcc_control_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountLevelControlsApi->set_account_level_mcc_control_post: %s\n" % e)
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

# **set_account_level_merchant_control_post**
> set_account_level_merchant_control_post(response_content_type=response_content_type)

Set Account-Level Merchant Control

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
    api_instance = openapi_client.AccountLevelControlsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Set Account-Level Merchant Control
        api_instance.set_account_level_merchant_control_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountLevelControlsApi->set_account_level_merchant_control_post: %s\n" % e)
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

