# openapi_client.TransactionsAchApi

All URIs are relative to *https://api-sandbox.cv.gpsrv.com/intserv/4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ach_account_corporate_post**](TransactionsAchApi.md#add_ach_account_corporate_post) | **POST** /addAchAccountCorporate | Add ACH Account Corporate
[**add_ach_account_post**](TransactionsAchApi.md#add_ach_account_post) | **POST** /addAchAccount | Add ACH Account
[**cancel_ach_transaction_post**](TransactionsAchApi.md#cancel_ach_transaction_post) | **POST** /cancelAchTransaction | Cancel ACH Transaction
[**cancel_simulated_ach_transaction_post**](TransactionsAchApi.md#cancel_simulated_ach_transaction_post) | **POST** /cancelSimulatedAchTransaction | Cancel Simulated Incoming ACH Transaction
[**create_ach_transaction_post**](TransactionsAchApi.md#create_ach_transaction_post) | **POST** /createAchTransaction | Create ACH Transaction
[**create_simulated_ach_transaction_post**](TransactionsAchApi.md#create_simulated_ach_transaction_post) | **POST** /createSimulatedAchTransaction | Create Simulated Incoming ACH Transaction
[**get_ach_accounts_post**](TransactionsAchApi.md#get_ach_accounts_post) | **POST** /getAchAccounts | Get ACH Accounts
[**get_ach_trans_history_post**](TransactionsAchApi.md#get_ach_trans_history_post) | **POST** /getAchTransHistory | Get ACH Transaction History
[**get_all_simulated_ach_transactions_post**](TransactionsAchApi.md#get_all_simulated_ach_transactions_post) | **POST** /getAllSimulatedAchTransactions | Get All Simulated Incoming ACH Transactions
[**get_deposit_history_post**](TransactionsAchApi.md#get_deposit_history_post) | **POST** /getDepositHistory | Get Deposit History
[**get_pending_deposits_post**](TransactionsAchApi.md#get_pending_deposits_post) | **POST** /getPendingDeposits | Get Pending Deposits
[**get_simulated_ach_transaction_post**](TransactionsAchApi.md#get_simulated_ach_transaction_post) | **POST** /getSimulatedAchTransaction | Get Simulated Incoming ACH Transaction
[**modify_ach_account_post**](TransactionsAchApi.md#modify_ach_account_post) | **POST** /modifyAchAccount | Modify ACH Account
[**modify_pending_deposit_status_post**](TransactionsAchApi.md#modify_pending_deposit_status_post) | **POST** /modifyPendingDepositStatus | Modify Pending Deposit Status
[**remove_ach_account_post**](TransactionsAchApi.md#remove_ach_account_post) | **POST** /removeAchAccount | Remove ACH Account


# **add_ach_account_corporate_post**
> add_ach_account_corporate_post(response_content_type=response_content_type)

Add ACH Account Corporate

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
    api_instance = openapi_client.TransactionsAchApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Add ACH Account Corporate
        api_instance.add_ach_account_corporate_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsAchApi->add_ach_account_corporate_post: %s\n" % e)
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

# **add_ach_account_post**
> add_ach_account_post(response_content_type=response_content_type)

Add ACH Account

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
    api_instance = openapi_client.TransactionsAchApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Add ACH Account
        api_instance.add_ach_account_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsAchApi->add_ach_account_post: %s\n" % e)
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

# **cancel_ach_transaction_post**
> cancel_ach_transaction_post(response_content_type=response_content_type)

Cancel ACH Transaction

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
    api_instance = openapi_client.TransactionsAchApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Cancel ACH Transaction
        api_instance.cancel_ach_transaction_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsAchApi->cancel_ach_transaction_post: %s\n" % e)
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

# **cancel_simulated_ach_transaction_post**
> cancel_simulated_ach_transaction_post(response_content_type=response_content_type)

Cancel Simulated Incoming ACH Transaction

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
    api_instance = openapi_client.TransactionsAchApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Cancel Simulated Incoming ACH Transaction
        api_instance.cancel_simulated_ach_transaction_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsAchApi->cancel_simulated_ach_transaction_post: %s\n" % e)
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

# **create_ach_transaction_post**
> create_ach_transaction_post(response_content_type=response_content_type)

Create ACH Transaction

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
    api_instance = openapi_client.TransactionsAchApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Create ACH Transaction
        api_instance.create_ach_transaction_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsAchApi->create_ach_transaction_post: %s\n" % e)
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

# **create_simulated_ach_transaction_post**
> create_simulated_ach_transaction_post(response_content_type=response_content_type)

Create Simulated Incoming ACH Transaction

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
    api_instance = openapi_client.TransactionsAchApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Create Simulated Incoming ACH Transaction
        api_instance.create_simulated_ach_transaction_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsAchApi->create_simulated_ach_transaction_post: %s\n" % e)
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

# **get_ach_accounts_post**
> get_ach_accounts_post(response_content_type=response_content_type)

Get ACH Accounts

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
    api_instance = openapi_client.TransactionsAchApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get ACH Accounts
        api_instance.get_ach_accounts_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsAchApi->get_ach_accounts_post: %s\n" % e)
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

# **get_ach_trans_history_post**
> get_ach_trans_history_post(response_content_type=response_content_type)

Get ACH Transaction History

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
    api_instance = openapi_client.TransactionsAchApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get ACH Transaction History
        api_instance.get_ach_trans_history_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsAchApi->get_ach_trans_history_post: %s\n" % e)
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

# **get_all_simulated_ach_transactions_post**
> get_all_simulated_ach_transactions_post(response_content_type=response_content_type)

Get All Simulated Incoming ACH Transactions

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
    api_instance = openapi_client.TransactionsAchApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get All Simulated Incoming ACH Transactions
        api_instance.get_all_simulated_ach_transactions_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsAchApi->get_all_simulated_ach_transactions_post: %s\n" % e)
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

# **get_deposit_history_post**
> get_deposit_history_post(response_content_type=response_content_type)

Get Deposit History

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
    api_instance = openapi_client.TransactionsAchApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Deposit History
        api_instance.get_deposit_history_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsAchApi->get_deposit_history_post: %s\n" % e)
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

# **get_pending_deposits_post**
> get_pending_deposits_post(response_content_type=response_content_type)

Get Pending Deposits

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
    api_instance = openapi_client.TransactionsAchApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Pending Deposits
        api_instance.get_pending_deposits_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsAchApi->get_pending_deposits_post: %s\n" % e)
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

# **get_simulated_ach_transaction_post**
> get_simulated_ach_transaction_post(response_content_type=response_content_type)

Get Simulated Incoming ACH Transaction

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
    api_instance = openapi_client.TransactionsAchApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Simulated Incoming ACH Transaction
        api_instance.get_simulated_ach_transaction_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsAchApi->get_simulated_ach_transaction_post: %s\n" % e)
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

# **modify_ach_account_post**
> modify_ach_account_post(response_content_type=response_content_type)

Modify ACH Account

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
    api_instance = openapi_client.TransactionsAchApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Modify ACH Account
        api_instance.modify_ach_account_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsAchApi->modify_ach_account_post: %s\n" % e)
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

# **modify_pending_deposit_status_post**
> modify_pending_deposit_status_post(response_content_type=response_content_type)

Modify Pending Deposit Status

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
    api_instance = openapi_client.TransactionsAchApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Modify Pending Deposit Status
        api_instance.modify_pending_deposit_status_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsAchApi->modify_pending_deposit_status_post: %s\n" % e)
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

# **remove_ach_account_post**
> remove_ach_account_post(response_content_type=response_content_type)

Remove ACH Account

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
    api_instance = openapi_client.TransactionsAchApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Remove ACH Account
        api_instance.remove_ach_account_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsAchApi->remove_ach_account_post: %s\n" % e)
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

