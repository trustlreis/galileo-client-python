# openapi_client.TransactionsBillPaymentsApi

All URIs are relative to *https://api-sandbox.cv.gpsrv.com/intserv/4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_paper_biller_post**](TransactionsBillPaymentsApi.md#add_paper_biller_post) | **POST** /addPaperBiller | Add Paper Biller
[**add_rpps_biller_post**](TransactionsBillPaymentsApi.md#add_rpps_biller_post) | **POST** /addRppsBiller | Add RPPS Biller
[**cancel_bill_payment_post**](TransactionsBillPaymentsApi.md#cancel_bill_payment_post) | **POST** /cancelBillPayment | Cancel Bill Payment
[**create_bill_payment_post**](TransactionsBillPaymentsApi.md#create_bill_payment_post) | **POST** /createBillPayment | Create Bill Payment
[**get_bill_pay_history_post**](TransactionsBillPaymentsApi.md#get_bill_pay_history_post) | **POST** /getBillPayHistory | Get Bill Payment History
[**get_billers_post**](TransactionsBillPaymentsApi.md#get_billers_post) | **POST** /getBillers | Get Billers
[**get_scheduled_bill_payments_post**](TransactionsBillPaymentsApi.md#get_scheduled_bill_payments_post) | **POST** /getScheduledBillPayments | Get Scheduled Bill Payments
[**modify_paper_biller_post**](TransactionsBillPaymentsApi.md#modify_paper_biller_post) | **POST** /modifyPaperBiller | Modify Paper Biller
[**modify_rpps_biller_post**](TransactionsBillPaymentsApi.md#modify_rpps_biller_post) | **POST** /modifyRppsBiller | Modify RPPS Biller
[**remove_biller_post**](TransactionsBillPaymentsApi.md#remove_biller_post) | **POST** /removeBiller | Remove Biller
[**search_biller_directory_post**](TransactionsBillPaymentsApi.md#search_biller_directory_post) | **POST** /searchBillerDirectory | Search Biller Directory


# **add_paper_biller_post**
> add_paper_biller_post(response_content_type=response_content_type)

Add Paper Biller

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
    api_instance = openapi_client.TransactionsBillPaymentsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Add Paper Biller
        api_instance.add_paper_biller_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsBillPaymentsApi->add_paper_biller_post: %s\n" % e)
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

# **add_rpps_biller_post**
> add_rpps_biller_post(response_content_type=response_content_type)

Add RPPS Biller

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
    api_instance = openapi_client.TransactionsBillPaymentsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Add RPPS Biller
        api_instance.add_rpps_biller_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsBillPaymentsApi->add_rpps_biller_post: %s\n" % e)
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

# **cancel_bill_payment_post**
> cancel_bill_payment_post(response_content_type=response_content_type)

Cancel Bill Payment

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
    api_instance = openapi_client.TransactionsBillPaymentsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Cancel Bill Payment
        api_instance.cancel_bill_payment_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsBillPaymentsApi->cancel_bill_payment_post: %s\n" % e)
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

# **create_bill_payment_post**
> create_bill_payment_post(response_content_type=response_content_type)

Create Bill Payment

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
    api_instance = openapi_client.TransactionsBillPaymentsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Create Bill Payment
        api_instance.create_bill_payment_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsBillPaymentsApi->create_bill_payment_post: %s\n" % e)
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

# **get_bill_pay_history_post**
> get_bill_pay_history_post(response_content_type=response_content_type)

Get Bill Payment History

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
    api_instance = openapi_client.TransactionsBillPaymentsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Bill Payment History
        api_instance.get_bill_pay_history_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsBillPaymentsApi->get_bill_pay_history_post: %s\n" % e)
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

# **get_billers_post**
> get_billers_post(response_content_type=response_content_type)

Get Billers

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
    api_instance = openapi_client.TransactionsBillPaymentsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Billers
        api_instance.get_billers_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsBillPaymentsApi->get_billers_post: %s\n" % e)
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

# **get_scheduled_bill_payments_post**
> get_scheduled_bill_payments_post(response_content_type=response_content_type)

Get Scheduled Bill Payments

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
    api_instance = openapi_client.TransactionsBillPaymentsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Scheduled Bill Payments
        api_instance.get_scheduled_bill_payments_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsBillPaymentsApi->get_scheduled_bill_payments_post: %s\n" % e)
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

# **modify_paper_biller_post**
> modify_paper_biller_post(response_content_type=response_content_type)

Modify Paper Biller

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
    api_instance = openapi_client.TransactionsBillPaymentsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Modify Paper Biller
        api_instance.modify_paper_biller_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsBillPaymentsApi->modify_paper_biller_post: %s\n" % e)
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

# **modify_rpps_biller_post**
> modify_rpps_biller_post(response_content_type=response_content_type)

Modify RPPS Biller

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
    api_instance = openapi_client.TransactionsBillPaymentsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Modify RPPS Biller
        api_instance.modify_rpps_biller_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsBillPaymentsApi->modify_rpps_biller_post: %s\n" % e)
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

# **remove_biller_post**
> remove_biller_post(response_content_type=response_content_type)

Remove Biller

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
    api_instance = openapi_client.TransactionsBillPaymentsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Remove Biller
        api_instance.remove_biller_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsBillPaymentsApi->remove_biller_post: %s\n" % e)
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

# **search_biller_directory_post**
> search_biller_directory_post(response_content_type=response_content_type)

Search Biller Directory

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
    api_instance = openapi_client.TransactionsBillPaymentsApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Search Biller Directory
        api_instance.search_biller_directory_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling TransactionsBillPaymentsApi->search_biller_directory_post: %s\n" % e)
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

