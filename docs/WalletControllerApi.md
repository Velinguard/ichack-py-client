# swagger_client.WalletControllerApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_wallet_using_delete**](WalletControllerApi.md#close_wallet_using_delete) | **DELETE** /close-wallet | Closes a wallet inside the distributed ledger, this must be done before another operation can be complete
[**create_wallet_using_put**](WalletControllerApi.md#create_wallet_using_put) | **PUT** /create-wallet | Creates a new wallet inside the distributed ledger
[**create_wallet_with_did_using_put**](WalletControllerApi.md#create_wallet_with_did_using_put) | **PUT** /create-wallet-with-did | Creates a new wallet inside the distributed ledger using a specific DiD
[**delete_wallet_using_delete**](WalletControllerApi.md#delete_wallet_using_delete) | **DELETE** /delete-wallet | Deletes a wallet inside the distributed ledger
[**login_using_get**](WalletControllerApi.md#login_using_get) | **GET** /login | Logs into a wallet inside the distributed ledger


# **close_wallet_using_delete**
> str close_wallet_using_delete(wallet_handle=wallet_handle)

Closes a wallet inside the distributed ledger, this must be done before another operation can be complete

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WalletControllerApi()
wallet_handle = 56 # int |  (optional)

try:
    # Closes a wallet inside the distributed ledger, this must be done before another operation can be complete
    api_response = api_instance.close_wallet_using_delete(wallet_handle=wallet_handle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletControllerApi->close_wallet_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_handle** | **int**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_wallet_using_put**
> str create_wallet_using_put(id=id, key=key)

Creates a new wallet inside the distributed ledger

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WalletControllerApi()
id = 'id_example' # str | id (optional)
key = 'key_example' # str | key (optional)

try:
    # Creates a new wallet inside the distributed ledger
    api_response = api_instance.create_wallet_using_put(id=id, key=key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletControllerApi->create_wallet_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | [optional] 
 **key** | **str**| key | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_wallet_with_did_using_put**
> str create_wallet_with_did_using_put(id=id, key=key)

Creates a new wallet inside the distributed ledger using a specific DiD

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WalletControllerApi()
id = 'id_example' # str | id (optional)
key = 'key_example' # str | key (optional)

try:
    # Creates a new wallet inside the distributed ledger using a specific DiD
    api_response = api_instance.create_wallet_with_did_using_put(id=id, key=key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletControllerApi->create_wallet_with_did_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | [optional] 
 **key** | **str**| key | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wallet_using_delete**
> str delete_wallet_using_delete(id=id, key=key)

Deletes a wallet inside the distributed ledger

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WalletControllerApi()
id = 'id_example' # str | id (optional)
key = 'key_example' # str | key (optional)

try:
    # Deletes a wallet inside the distributed ledger
    api_response = api_instance.delete_wallet_using_delete(id=id, key=key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletControllerApi->delete_wallet_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | [optional] 
 **key** | **str**| key | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_using_get**
> object login_using_get(did=did, id=id, key=key, master_did=master_did)

Logs into a wallet inside the distributed ledger

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WalletControllerApi()
did = 'did_example' # str | did (optional)
id = 'id_example' # str | id (optional)
key = 'key_example' # str | key (optional)
master_did = 'master_did_example' # str | masterDid (optional)

try:
    # Logs into a wallet inside the distributed ledger
    api_response = api_instance.login_using_get(did=did, id=id, key=key, master_did=master_did)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletControllerApi->login_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| did | [optional] 
 **id** | **str**| id | [optional] 
 **key** | **str**| key | [optional] 
 **master_did** | **str**| masterDid | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

