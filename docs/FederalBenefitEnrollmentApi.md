# openapi_client.FederalBenefitEnrollmentApi

All URIs are relative to *https://api-sandbox.cv.gpsrv.com/intserv/4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fb_enrollment_post**](FederalBenefitEnrollmentApi.md#create_fb_enrollment_post) | **POST** /createFbEnrollment | Create Federal Benefit Enrollment
[**get_fb_enrollments_post**](FederalBenefitEnrollmentApi.md#get_fb_enrollments_post) | **POST** /getFbEnrollments | Get Federal Benefit Enrollments
[**resubmit_fb_enrollment_post**](FederalBenefitEnrollmentApi.md#resubmit_fb_enrollment_post) | **POST** /resubmitFbEnrollment | Resubmit Federal Benefit Enrollment
[**update_fb_enrollment_post**](FederalBenefitEnrollmentApi.md#update_fb_enrollment_post) | **POST** /updateFbEnrollment | Update Federal Benefit Enrollment


# **create_fb_enrollment_post**
> create_fb_enrollment_post(response_content_type=response_content_type)

Create Federal Benefit Enrollment

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
    api_instance = openapi_client.FederalBenefitEnrollmentApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Create Federal Benefit Enrollment
        api_instance.create_fb_enrollment_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling FederalBenefitEnrollmentApi->create_fb_enrollment_post: %s\n" % e)
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

# **get_fb_enrollments_post**
> get_fb_enrollments_post(response_content_type=response_content_type)

Get Federal Benefit Enrollments

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
    api_instance = openapi_client.FederalBenefitEnrollmentApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Get Federal Benefit Enrollments
        api_instance.get_fb_enrollments_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling FederalBenefitEnrollmentApi->get_fb_enrollments_post: %s\n" % e)
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

# **resubmit_fb_enrollment_post**
> resubmit_fb_enrollment_post(response_content_type=response_content_type)

Resubmit Federal Benefit Enrollment

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
    api_instance = openapi_client.FederalBenefitEnrollmentApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Resubmit Federal Benefit Enrollment
        api_instance.resubmit_fb_enrollment_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling FederalBenefitEnrollmentApi->resubmit_fb_enrollment_post: %s\n" % e)
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

# **update_fb_enrollment_post**
> update_fb_enrollment_post(response_content_type=response_content_type)

Update Federal Benefit Enrollment

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
    api_instance = openapi_client.FederalBenefitEnrollmentApi(api_client)
    response_content_type = 'json' # str |  (optional)

    try:
        # Update Federal Benefit Enrollment
        api_instance.update_fb_enrollment_post(response_content_type=response_content_type)
    except Exception as e:
        print("Exception when calling FederalBenefitEnrollmentApi->update_fb_enrollment_post: %s\n" % e)
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

