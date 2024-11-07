# openapi_client.AccountsAndCardsEnrollmentApi

All URIs are relative to *https://api-sandbox.cv.gpsrv.com/intserv/4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**complete_enrollment_post**](AccountsAndCardsEnrollmentApi.md#complete_enrollment_post) | **POST** /completeEnrollment | Complete Enrollment
[**create_account_post**](AccountsAndCardsEnrollmentApi.md#create_account_post) | **POST** /createAccount | Create Account
[**create_virtual_card_post**](AccountsAndCardsEnrollmentApi.md#create_virtual_card_post) | **POST** /createVirtualCard | Create Virtual Card Account
[**force_pass_cip_post**](AccountsAndCardsEnrollmentApi.md#force_pass_cip_post) | **POST** /forcePassCip | Force Pass CIP
[**get_enrollment_info_post**](AccountsAndCardsEnrollmentApi.md#get_enrollment_info_post) | **POST** /getEnrollmentInfo | Get Enrollment Info
[**run_cip_post**](AccountsAndCardsEnrollmentApi.md#run_cip_post) | **POST** /runCip | Run CIP
[**run_enrollment_cip_post**](AccountsAndCardsEnrollmentApi.md#run_enrollment_cip_post) | **POST** /runEnrollmentCip | Run Enrollment CIP
[**start_enrollment_post**](AccountsAndCardsEnrollmentApi.md#start_enrollment_post) | **POST** /startEnrollment | Start Enrollment
[**update_enrollment_post**](AccountsAndCardsEnrollmentApi.md#update_enrollment_post) | **POST** /updateEnrollment | Update Enrollment
[**verify_enrollment_post**](AccountsAndCardsEnrollmentApi.md#verify_enrollment_post) | **POST** /verifyEnrollment | Verify Enrollment


# **complete_enrollment_post**
> complete_enrollment_post(response_content_type=response_content_type)

Complete Enrollment

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
    api_instance = openapi_client.AccountsAndCardsEnrollmentApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Complete Enrollment
        api_instance.complete_enrollment_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsEnrollmentApi->complete_enrollment_post: %s\n" % e)
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

# **create_account_post**
> create_account_post(response_content_type=response_content_type)

Create Account

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
    api_instance = openapi_client.AccountsAndCardsEnrollmentApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Create Account
        api_instance.create_account_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsEnrollmentApi->create_account_post: %s\n" % e)
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

# **create_virtual_card_post**
> create_virtual_card_post(response_content_type=response_content_type)

Create Virtual Card Account

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
    api_instance = openapi_client.AccountsAndCardsEnrollmentApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Create Virtual Card Account
        api_instance.create_virtual_card_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsEnrollmentApi->create_virtual_card_post: %s\n" % e)
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

# **force_pass_cip_post**
> force_pass_cip_post(response_content_type=response_content_type)

Force Pass CIP

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
    api_instance = openapi_client.AccountsAndCardsEnrollmentApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Force Pass CIP
        api_instance.force_pass_cip_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsEnrollmentApi->force_pass_cip_post: %s\n" % e)
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

# **get_enrollment_info_post**
> get_enrollment_info_post(response_content_type=response_content_type)

Get Enrollment Info

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
    api_instance = openapi_client.AccountsAndCardsEnrollmentApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Enrollment Info
        api_instance.get_enrollment_info_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsEnrollmentApi->get_enrollment_info_post: %s\n" % e)
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

# **run_cip_post**
> run_cip_post(response_content_type=response_content_type)

Run CIP

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
    api_instance = openapi_client.AccountsAndCardsEnrollmentApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Run CIP
        api_instance.run_cip_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsEnrollmentApi->run_cip_post: %s\n" % e)
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

# **run_enrollment_cip_post**
> run_enrollment_cip_post(response_content_type=response_content_type)

Run Enrollment CIP

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
    api_instance = openapi_client.AccountsAndCardsEnrollmentApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Run Enrollment CIP
        api_instance.run_enrollment_cip_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsEnrollmentApi->run_enrollment_cip_post: %s\n" % e)
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

# **start_enrollment_post**
> start_enrollment_post(response_content_type=response_content_type)

Start Enrollment

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
    api_instance = openapi_client.AccountsAndCardsEnrollmentApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Start Enrollment
        api_instance.start_enrollment_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsEnrollmentApi->start_enrollment_post: %s\n" % e)
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

# **update_enrollment_post**
> update_enrollment_post(response_content_type=response_content_type)

Update Enrollment

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
    api_instance = openapi_client.AccountsAndCardsEnrollmentApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Update Enrollment
        api_instance.update_enrollment_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsEnrollmentApi->update_enrollment_post: %s\n" % e)
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

# **verify_enrollment_post**
> verify_enrollment_post(response_content_type=response_content_type)

Verify Enrollment

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
    api_instance = openapi_client.AccountsAndCardsEnrollmentApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Verify Enrollment
        api_instance.verify_enrollment_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling AccountsAndCardsEnrollmentApi->verify_enrollment_post: %s\n" % e)
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

