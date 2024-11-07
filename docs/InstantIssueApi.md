# openapi_client.InstantIssueApi

All URIs are relative to *https://api-sandbox.cv.gpsrv.com/intserv/4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bulk_card_order_post**](InstantIssueApi.md#create_bulk_card_order_post) | **POST** /createBulkCardOrder | Create Bulk Card Order
[**get_bulk_card_order_post**](InstantIssueApi.md#get_bulk_card_order_post) | **POST** /getBulkCardOrder | Get Bulk Card Order
[**get_load_locations_post**](InstantIssueApi.md#get_load_locations_post) | **POST** /getLoadLocations | Get Load Locations
[**move_card_inventory_post**](InstantIssueApi.md#move_card_inventory_post) | **POST** /moveCardInventory | Move Card Inventory
[**move_card_post**](InstantIssueApi.md#move_card_post) | **POST** /moveCard | Move Card
[**verify_instant_issue_card_post**](InstantIssueApi.md#verify_instant_issue_card_post) | **POST** /verifyInstantIssueCard | Verify Instant-Issue Card


# **create_bulk_card_order_post**
> create_bulk_card_order_post(response_content_type=response_content_type)

Create Bulk Card Order

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
    api_instance = openapi_client.InstantIssueApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Create Bulk Card Order
        api_instance.create_bulk_card_order_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling InstantIssueApi->create_bulk_card_order_post: %s\n" % e)
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

# **get_bulk_card_order_post**
> get_bulk_card_order_post(response_content_type=response_content_type)

Get Bulk Card Order

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
    api_instance = openapi_client.InstantIssueApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Bulk Card Order
        api_instance.get_bulk_card_order_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling InstantIssueApi->get_bulk_card_order_post: %s\n" % e)
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

# **get_load_locations_post**
> get_load_locations_post(response_content_type=response_content_type)

Get Load Locations

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
    api_instance = openapi_client.InstantIssueApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Load Locations
        api_instance.get_load_locations_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling InstantIssueApi->get_load_locations_post: %s\n" % e)
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

# **move_card_inventory_post**
> move_card_inventory_post(response_content_type=response_content_type)

Move Card Inventory

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
    api_instance = openapi_client.InstantIssueApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Move Card Inventory
        api_instance.move_card_inventory_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling InstantIssueApi->move_card_inventory_post: %s\n" % e)
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

# **move_card_post**
> move_card_post(response_content_type=response_content_type)

Move Card

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
    api_instance = openapi_client.InstantIssueApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Move Card
        api_instance.move_card_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling InstantIssueApi->move_card_post: %s\n" % e)
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

# **verify_instant_issue_card_post**
> verify_instant_issue_card_post(response_content_type=response_content_type)

Verify Instant-Issue Card

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
    api_instance = openapi_client.InstantIssueApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Verify Instant-Issue Card
        api_instance.verify_instant_issue_card_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling InstantIssueApi->verify_instant_issue_card_post: %s\n" % e)
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

