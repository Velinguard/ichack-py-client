# swagger_client.IcHackAirlineControllerApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buy_using_get**](IcHackAirlineControllerApi.md#buy_using_get) | **GET** /hold-place | buy
[**get_event_list_using_get**](IcHackAirlineControllerApi.md#get_event_list_using_get) | **GET** /get-events | getEventList
[**get_specific_event_using_get**](IcHackAirlineControllerApi.md#get_specific_event_using_get) | **GET** /get-event | getSpecificEvent


# **buy_using_get**
> buy_using_get(area=area, event=event, seat=seat)

buy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IcHackAirlineControllerApi()
area = 'area_example' # str | area (optional)
event = 'event_example' # str | event (optional)
seat = 'seat_example' # str | seat (optional)

try:
    # buy
    api_instance.buy_using_get(area=area, event=event, seat=seat)
except ApiException as e:
    print("Exception when calling IcHackAirlineControllerApi->buy_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area** | **str**| area | [optional] 
 **event** | **str**| event | [optional] 
 **seat** | **str**| seat | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_list_using_get**
> list[str] get_event_list_using_get()

getEventList

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IcHackAirlineControllerApi()

try:
    # getEventList
    api_response = api_instance.get_event_list_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IcHackAirlineControllerApi->get_event_list_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_specific_event_using_get**
> Event get_specific_event_using_get(name=name)

getSpecificEvent

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IcHackAirlineControllerApi()
name = 'name_example' # str | name (optional)

try:
    # getSpecificEvent
    api_response = api_instance.get_specific_event_using_get(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IcHackAirlineControllerApi->get_specific_event_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | [optional] 

### Return type

[**Event**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

