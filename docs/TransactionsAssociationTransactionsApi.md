# openapi_client.TransactionsAssociationTransactionsApi

All URIs are relative to *https://api-sandbox.cv.gpsrv.com/intserv/4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_simulated_card_auth_post**](TransactionsAssociationTransactionsApi.md#create_simulated_card_auth_post) | **POST** /createSimulatedCardAuth | Create Simulated Card Authorization
[**create_simulated_card_settle_post**](TransactionsAssociationTransactionsApi.md#create_simulated_card_settle_post) | **POST** /createSimulatedCardSettle | Create Simulated Card Settlement
[**expire_authorization_post**](TransactionsAssociationTransactionsApi.md#expire_authorization_post) | **POST** /expireAuthorization | Expire Authorization
[**get_auth_history_post**](TransactionsAssociationTransactionsApi.md#get_auth_history_post) | **POST** /getAuthHistory | Get Authorization History
[**get_pending_merchant_credits_post**](TransactionsAssociationTransactionsApi.md#get_pending_merchant_credits_post) | **POST** /getPendingMerchantCredits | Get Pending Merchant Credits
[**update_pending_merchant_credit_post**](TransactionsAssociationTransactionsApi.md#update_pending_merchant_credit_post) | **POST** /updatePendingMerchantCredit | Update Pending Merchant Credit


# **create_simulated_card_auth_post**
> create_simulated_card_auth_post(response_content_type=response_content_type)

Create Simulated Card Authorization

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
    api_instance = openapi_client.TransactionsAssociationTransactionsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Create Simulated Card Authorization
        api_instance.create_simulated_card_auth_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsAssociationTransactionsApi->create_simulated_card_auth_post: %s\n" % e)
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

# **create_simulated_card_settle_post**
> create_simulated_card_settle_post(response_content_type=response_content_type)

Create Simulated Card Settlement

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
    api_instance = openapi_client.TransactionsAssociationTransactionsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Create Simulated Card Settlement
        api_instance.create_simulated_card_settle_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsAssociationTransactionsApi->create_simulated_card_settle_post: %s\n" % e)
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

# **expire_authorization_post**
> expire_authorization_post(response_content_type=response_content_type)

Expire Authorization

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
    api_instance = openapi_client.TransactionsAssociationTransactionsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Expire Authorization
        api_instance.expire_authorization_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsAssociationTransactionsApi->expire_authorization_post: %s\n" % e)
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

# **get_auth_history_post**
> get_auth_history_post(response_content_type=response_content_type)

Get Authorization History

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
    api_instance = openapi_client.TransactionsAssociationTransactionsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Authorization History
        api_instance.get_auth_history_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsAssociationTransactionsApi->get_auth_history_post: %s\n" % e)
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

# **get_pending_merchant_credits_post**
> get_pending_merchant_credits_post(response_content_type=response_content_type)

Get Pending Merchant Credits

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
    api_instance = openapi_client.TransactionsAssociationTransactionsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Pending Merchant Credits
        api_instance.get_pending_merchant_credits_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsAssociationTransactionsApi->get_pending_merchant_credits_post: %s\n" % e)
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

# **update_pending_merchant_credit_post**
> update_pending_merchant_credit_post(response_content_type=response_content_type)

Update Pending Merchant Credit

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
    api_instance = openapi_client.TransactionsAssociationTransactionsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Update Pending Merchant Credit
        api_instance.update_pending_merchant_credit_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsAssociationTransactionsApi->update_pending_merchant_credit_post: %s\n" % e)
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

