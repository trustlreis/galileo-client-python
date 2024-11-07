# openapi_client.CorporateHierarchyApi

All URIs are relative to *https://api-sandbox.cv.gpsrv.com/intserv/4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group_post**](CorporateHierarchyApi.md#create_group_post) | **POST** /createGroup | Create Group
[**delete_groups_post**](CorporateHierarchyApi.md#delete_groups_post) | **POST** /deleteGroups | Delete Groups
[**get_account_group_relationships_post**](CorporateHierarchyApi.md#get_account_group_relationships_post) | **POST** /getAccountGroupRelationships | Get Account Group Relationships
[**get_group_hierarchy_post**](CorporateHierarchyApi.md#get_group_hierarchy_post) | **POST** /getGroupHierarchy | Get Group Hierarchy
[**get_groups_info_post**](CorporateHierarchyApi.md#get_groups_info_post) | **POST** /getGroupsInfo | Get Groups Info
[**get_root_groups_post**](CorporateHierarchyApi.md#get_root_groups_post) | **POST** /getRootGroups | Get Root Groups
[**remove_account_group_relationship_post**](CorporateHierarchyApi.md#remove_account_group_relationship_post) | **POST** /removeAccountGroupRelationship | Remove Account Group Relationship
[**set_account_group_relationships_post**](CorporateHierarchyApi.md#set_account_group_relationships_post) | **POST** /setAccountGroupRelationships | Set Account Group Relationships
[**update_group_post**](CorporateHierarchyApi.md#update_group_post) | **POST** /updateGroup | Update Group


# **create_group_post**
> create_group_post(response_content_type=response_content_type)

Create Group

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
    api_instance = openapi_client.CorporateHierarchyApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Create Group
        api_instance.create_group_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling CorporateHierarchyApi->create_group_post: %s\n" % e)
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

# **delete_groups_post**
> delete_groups_post(response_content_type=response_content_type)

Delete Groups

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
    api_instance = openapi_client.CorporateHierarchyApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Delete Groups
        api_instance.delete_groups_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling CorporateHierarchyApi->delete_groups_post: %s\n" % e)
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

# **get_account_group_relationships_post**
> get_account_group_relationships_post(response_content_type=response_content_type)

Get Account Group Relationships

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
    api_instance = openapi_client.CorporateHierarchyApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Account Group Relationships
        api_instance.get_account_group_relationships_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling CorporateHierarchyApi->get_account_group_relationships_post: %s\n" % e)
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

# **get_group_hierarchy_post**
> get_group_hierarchy_post(response_content_type=response_content_type)

Get Group Hierarchy

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
    api_instance = openapi_client.CorporateHierarchyApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Group Hierarchy
        api_instance.get_group_hierarchy_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling CorporateHierarchyApi->get_group_hierarchy_post: %s\n" % e)
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

# **get_groups_info_post**
> get_groups_info_post(response_content_type=response_content_type)

Get Groups Info

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
    api_instance = openapi_client.CorporateHierarchyApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Groups Info
        api_instance.get_groups_info_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling CorporateHierarchyApi->get_groups_info_post: %s\n" % e)
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

# **get_root_groups_post**
> get_root_groups_post(response_content_type=response_content_type)

Get Root Groups

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
    api_instance = openapi_client.CorporateHierarchyApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Root Groups
        api_instance.get_root_groups_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling CorporateHierarchyApi->get_root_groups_post: %s\n" % e)
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

# **remove_account_group_relationship_post**
> remove_account_group_relationship_post(response_content_type=response_content_type)

Remove Account Group Relationship

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
    api_instance = openapi_client.CorporateHierarchyApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Remove Account Group Relationship
        api_instance.remove_account_group_relationship_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling CorporateHierarchyApi->remove_account_group_relationship_post: %s\n" % e)
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

# **set_account_group_relationships_post**
> set_account_group_relationships_post(response_content_type=response_content_type)

Set Account Group Relationships

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
    api_instance = openapi_client.CorporateHierarchyApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Set Account Group Relationships
        api_instance.set_account_group_relationships_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling CorporateHierarchyApi->set_account_group_relationships_post: %s\n" % e)
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

# **update_group_post**
> update_group_post(response_content_type=response_content_type)

Update Group

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
    api_instance = openapi_client.CorporateHierarchyApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Update Group
        api_instance.update_group_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling CorporateHierarchyApi->update_group_post: %s\n" % e)
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

