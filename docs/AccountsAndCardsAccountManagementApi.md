# openapi_client.AccountsAndCardsAccountManagementApi

All URIs are relative to *https://api-sandbox.cv.gpsrv.com/intserv/4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_account_post**](AccountsAndCardsAccountManagementApi.md#add_account_post) | **POST** /addAccount | Add Account
[**charge_off_account_post**](AccountsAndCardsAccountManagementApi.md#charge_off_account_post) | **POST** /chargeOffAccount | Charge Off Account
[**get_account_by_id_post**](AccountsAndCardsAccountManagementApi.md#get_account_by_id_post) | **POST** /getAccountById | Get Account by ID
[**get_balance_post**](AccountsAndCardsAccountManagementApi.md#get_balance_post) | **POST** /getBalance | Get Balance
[**get_related_accounts_post**](AccountsAndCardsAccountManagementApi.md#get_related_accounts_post) | **POST** /getRelatedAccounts | Get Related Accounts
[**get_roundup_accounts_post**](AccountsAndCardsAccountManagementApi.md#get_roundup_accounts_post) | **POST** /getRoundupAccounts | Get Roundup Accounts
[**get_savings_interest_post**](AccountsAndCardsAccountManagementApi.md#get_savings_interest_post) | **POST** /getSavingsInterest | Get Savings Interest
[**get_user_defined_account_fields_post**](AccountsAndCardsAccountManagementApi.md#get_user_defined_account_fields_post) | **POST** /getUserDefinedAccountFields | Get User-Defined Account Fields
[**recover_charged_off_account_post**](AccountsAndCardsAccountManagementApi.md#recover_charged_off_account_post) | **POST** /recoverChargedOffAccount | Recover Charged-Off Account
[**search_accounts_post**](AccountsAndCardsAccountManagementApi.md#search_accounts_post) | **POST** /searchAccounts | Search Accounts
[**set_roundup_accounts_post**](AccountsAndCardsAccountManagementApi.md#set_roundup_accounts_post) | **POST** /setRoundupAccounts | Set Roundup Accounts
[**set_user_defined_account_field_post**](AccountsAndCardsAccountManagementApi.md#set_user_defined_account_field_post) | **POST** /setUserDefinedAccountField | Set User-Defined Account Field
[**switch_product_post**](AccountsAndCardsAccountManagementApi.md#switch_product_post) | **POST** /switchProduct | Switch Product
[**update_account_post**](AccountsAndCardsAccountManagementApi.md#update_account_post) | **POST** /updateAccount | Update Account
[**verify_account_post**](AccountsAndCardsAccountManagementApi.md#verify_account_post) | **POST** /verifyAccount | Verify Account


# **add_account_post**
> add_account_post(response_content_type=response_content_type)

Add Account

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
    api_instance = openapi_client.AccountsAndCardsAccountManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Add Account
        api_instance.add_account_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsAccountManagementApi->add_account_post: %s\n" % e)
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

# **charge_off_account_post**
> charge_off_account_post(response_content_type=response_content_type)

Charge Off Account

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
    api_instance = openapi_client.AccountsAndCardsAccountManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Charge Off Account
        api_instance.charge_off_account_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsAccountManagementApi->charge_off_account_post: %s\n" % e)
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

# **get_account_by_id_post**
> get_account_by_id_post(response_content_type=response_content_type)

Get Account by ID

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
    api_instance = openapi_client.AccountsAndCardsAccountManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Account by ID
        api_instance.get_account_by_id_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsAccountManagementApi->get_account_by_id_post: %s\n" % e)
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

# **get_balance_post**
> get_balance_post(response_content_type=response_content_type)

Get Balance

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
    api_instance = openapi_client.AccountsAndCardsAccountManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Balance
        api_instance.get_balance_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsAccountManagementApi->get_balance_post: %s\n" % e)
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

# **get_related_accounts_post**
> get_related_accounts_post(response_content_type=response_content_type)

Get Related Accounts

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
    api_instance = openapi_client.AccountsAndCardsAccountManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Related Accounts
        api_instance.get_related_accounts_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsAccountManagementApi->get_related_accounts_post: %s\n" % e)
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

# **get_roundup_accounts_post**
> get_roundup_accounts_post(response_content_type=response_content_type)

Get Roundup Accounts

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
    api_instance = openapi_client.AccountsAndCardsAccountManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Roundup Accounts
        api_instance.get_roundup_accounts_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsAccountManagementApi->get_roundup_accounts_post: %s\n" % e)
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

# **get_savings_interest_post**
> get_savings_interest_post(response_content_type=response_content_type)

Get Savings Interest

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
    api_instance = openapi_client.AccountsAndCardsAccountManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Savings Interest
        api_instance.get_savings_interest_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsAccountManagementApi->get_savings_interest_post: %s\n" % e)
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

# **get_user_defined_account_fields_post**
> get_user_defined_account_fields_post(response_content_type=response_content_type)

Get User-Defined Account Fields

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
    api_instance = openapi_client.AccountsAndCardsAccountManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get User-Defined Account Fields
        api_instance.get_user_defined_account_fields_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsAccountManagementApi->get_user_defined_account_fields_post: %s\n" % e)
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

# **recover_charged_off_account_post**
> recover_charged_off_account_post(response_content_type=response_content_type)

Recover Charged-Off Account

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
    api_instance = openapi_client.AccountsAndCardsAccountManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Recover Charged-Off Account
        api_instance.recover_charged_off_account_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsAccountManagementApi->recover_charged_off_account_post: %s\n" % e)
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

# **search_accounts_post**
> search_accounts_post(response_content_type=response_content_type)

Search Accounts

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
    api_instance = openapi_client.AccountsAndCardsAccountManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Search Accounts
        api_instance.search_accounts_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsAccountManagementApi->search_accounts_post: %s\n" % e)
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

# **set_roundup_accounts_post**
> set_roundup_accounts_post(response_content_type=response_content_type)

Set Roundup Accounts

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
    api_instance = openapi_client.AccountsAndCardsAccountManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Set Roundup Accounts
        api_instance.set_roundup_accounts_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsAccountManagementApi->set_roundup_accounts_post: %s\n" % e)
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

# **set_user_defined_account_field_post**
> set_user_defined_account_field_post(response_content_type=response_content_type)

Set User-Defined Account Field

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
    api_instance = openapi_client.AccountsAndCardsAccountManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Set User-Defined Account Field
        api_instance.set_user_defined_account_field_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsAccountManagementApi->set_user_defined_account_field_post: %s\n" % e)
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

# **switch_product_post**
> switch_product_post(response_content_type=response_content_type)

Switch Product

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
    api_instance = openapi_client.AccountsAndCardsAccountManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Switch Product
        api_instance.switch_product_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsAccountManagementApi->switch_product_post: %s\n" % e)
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

# **update_account_post**
> update_account_post(response_content_type=response_content_type)

Update Account

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
    api_instance = openapi_client.AccountsAndCardsAccountManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Update Account
        api_instance.update_account_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsAccountManagementApi->update_account_post: %s\n" % e)
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

# **verify_account_post**
> verify_account_post(response_content_type=response_content_type)

Verify Account

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
    api_instance = openapi_client.AccountsAndCardsAccountManagementApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Verify Account
        api_instance.verify_account_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsAccountManagementApi->verify_account_post: %s\n" % e)
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

