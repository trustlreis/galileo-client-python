# openapi_client.AccountsAndCardsCardManagementApi

All URIs are relative to *https://api-sandbox.cv.gpsrv.com/intserv/4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_card_post**](AccountsAndCardsCardManagementApi.md#activate_card_post) | **POST** /activateCard | Activate Card
[**add_card_post**](AccountsAndCardsCardManagementApi.md#add_card_post) | **POST** /addCard | Add Card
[**commit_card_pin_change_post**](AccountsAndCardsCardManagementApi.md#commit_card_pin_change_post) | **POST** /commitCardPinChange | Commit Card PIN Change
[**create_provisioning_request_post**](AccountsAndCardsCardManagementApi.md#create_provisioning_request_post) | **POST** /createProvisioningRequest | Create Provisioning Request
[**get_access_token_post**](AccountsAndCardsCardManagementApi.md#get_access_token_post) | **POST** /getAccessToken | Get Access Token
[**get_account_cards_post**](AccountsAndCardsCardManagementApi.md#get_account_cards_post) | **POST** /getAccountCards | Get Account Cards
[**get_card_pin_change_key_post**](AccountsAndCardsCardManagementApi.md#get_card_pin_change_key_post) | **POST** /getCardPinChangeKey | Get Card PIN-Change Key
[**get_card_post**](AccountsAndCardsCardManagementApi.md#get_card_post) | **POST** /getCard | Get Card
[**get_interest_post**](AccountsAndCardsCardManagementApi.md#get_interest_post) | **POST** /getInterest | Get Interest
[**reissue_card_post**](AccountsAndCardsCardManagementApi.md#reissue_card_post) | **POST** /reissueCard | Reissue Card
[**replace_lost_stolen_card_post**](AccountsAndCardsCardManagementApi.md#replace_lost_stolen_card_post) | **POST** /replaceLostStolenCard | Replace Lost Stolen Card
[**reset_card_pin_fail_count_post**](AccountsAndCardsCardManagementApi.md#reset_card_pin_fail_count_post) | **POST** /resetCardPinFailCount | Reset Card PIN-Fail Count
[**verify_card_security_code_post**](AccountsAndCardsCardManagementApi.md#verify_card_security_code_post) | **POST** /verifyCardSecurityCode | Verify Card Security Code
[**void_add_card_post**](AccountsAndCardsCardManagementApi.md#void_add_card_post) | **POST** /voidAddCard | Void Add Card


# **activate_card_post**
> activate_card_post(response_content_type=response_content_type)

Activate Card

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
    api_instance = openapi_client.AccountsAndCardsCardManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Activate Card
        api_instance.activate_card_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsCardManagementApi->activate_card_post: %s\n" % e)
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

# **add_card_post**
> add_card_post(response_content_type=response_content_type)

Add Card

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
    api_instance = openapi_client.AccountsAndCardsCardManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Add Card
        api_instance.add_card_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsCardManagementApi->add_card_post: %s\n" % e)
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

# **commit_card_pin_change_post**
> commit_card_pin_change_post(response_content_type=response_content_type)

Commit Card PIN Change

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
    api_instance = openapi_client.AccountsAndCardsCardManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Commit Card PIN Change
        api_instance.commit_card_pin_change_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsCardManagementApi->commit_card_pin_change_post: %s\n" % e)
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

# **create_provisioning_request_post**
> create_provisioning_request_post(response_content_type=response_content_type)

Create Provisioning Request

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
    api_instance = openapi_client.AccountsAndCardsCardManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Create Provisioning Request
        api_instance.create_provisioning_request_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsCardManagementApi->create_provisioning_request_post: %s\n" % e)
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

# **get_access_token_post**
> get_access_token_post(response_content_type=response_content_type)

Get Access Token

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
    api_instance = openapi_client.AccountsAndCardsCardManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Access Token
        api_instance.get_access_token_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsCardManagementApi->get_access_token_post: %s\n" % e)
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

# **get_account_cards_post**
> get_account_cards_post(response_content_type=response_content_type)

Get Account Cards

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
    api_instance = openapi_client.AccountsAndCardsCardManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Account Cards
        api_instance.get_account_cards_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsCardManagementApi->get_account_cards_post: %s\n" % e)
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

# **get_card_pin_change_key_post**
> get_card_pin_change_key_post(response_content_type=response_content_type)

Get Card PIN-Change Key

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
    api_instance = openapi_client.AccountsAndCardsCardManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Card PIN-Change Key
        api_instance.get_card_pin_change_key_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsCardManagementApi->get_card_pin_change_key_post: %s\n" % e)
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

# **get_card_post**
> get_card_post(response_content_type=response_content_type)

Get Card

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
    api_instance = openapi_client.AccountsAndCardsCardManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Card
        api_instance.get_card_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsCardManagementApi->get_card_post: %s\n" % e)
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

# **get_interest_post**
> get_interest_post(response_content_type=response_content_type)

Get Interest

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
    api_instance = openapi_client.AccountsAndCardsCardManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Interest
        api_instance.get_interest_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsCardManagementApi->get_interest_post: %s\n" % e)
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

# **reissue_card_post**
> reissue_card_post(response_content_type=response_content_type)

Reissue Card

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
    api_instance = openapi_client.AccountsAndCardsCardManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Reissue Card
        api_instance.reissue_card_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsCardManagementApi->reissue_card_post: %s\n" % e)
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

# **replace_lost_stolen_card_post**
> replace_lost_stolen_card_post(response_content_type=response_content_type)

Replace Lost Stolen Card

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
    api_instance = openapi_client.AccountsAndCardsCardManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Replace Lost Stolen Card
        api_instance.replace_lost_stolen_card_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsCardManagementApi->replace_lost_stolen_card_post: %s\n" % e)
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

# **reset_card_pin_fail_count_post**
> reset_card_pin_fail_count_post(response_content_type=response_content_type)

Reset Card PIN-Fail Count

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
    api_instance = openapi_client.AccountsAndCardsCardManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Reset Card PIN-Fail Count
        api_instance.reset_card_pin_fail_count_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsCardManagementApi->reset_card_pin_fail_count_post: %s\n" % e)
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

# **verify_card_security_code_post**
> verify_card_security_code_post(response_content_type=response_content_type)

Verify Card Security Code

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
    api_instance = openapi_client.AccountsAndCardsCardManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Verify Card Security Code
        api_instance.verify_card_security_code_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsCardManagementApi->verify_card_security_code_post: %s\n" % e)
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

# **void_add_card_post**
> void_add_card_post(response_content_type=response_content_type)

Void Add Card

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
    api_instance = openapi_client.AccountsAndCardsCardManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Void Add Card
        api_instance.void_add_card_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsCardManagementApi->void_add_card_post: %s\n" % e)
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

