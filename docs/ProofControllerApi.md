# swagger_client.ProofControllerApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_licences_using_get**](ProofControllerApi.md#get_licences_using_get) | **GET** /get-licence-type | A list of licences available
[**get_proof_json_using_get**](ProofControllerApi.md#get_proof_json_using_get) | **GET** /get-proof | A proof json for a given proof
[**get_proof_request_using_get**](ProofControllerApi.md#get_proof_request_using_get) | **GET** /get-proof-request | getProofRequest
[**get_proofs_using_get**](ProofControllerApi.md#get_proofs_using_get) | **GET** /get-proofs | A list of available proofs for a licence


# **get_licences_using_get**
> list[str] get_licences_using_get()

A list of licences available

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProofControllerApi()

try:
    # A list of licences available
    api_response = api_instance.get_licences_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProofControllerApi->get_licences_using_get: %s\n" % e)
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

# **get_proof_json_using_get**
> str get_proof_json_using_get(proof=proof)

A proof json for a given proof

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProofControllerApi()
proof = 'proof_example' # str | proof (optional)

try:
    # A proof json for a given proof
    api_response = api_instance.get_proof_json_using_get(proof=proof)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProofControllerApi->get_proof_json_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proof** | **str**| proof | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_proof_request_using_get**
> str get_proof_request_using_get()

getProofRequest

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProofControllerApi()

try:
    # getProofRequest
    api_response = api_instance.get_proof_request_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProofControllerApi->get_proof_request_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_proofs_using_get**
> list[str] get_proofs_using_get(licence=licence)

A list of available proofs for a licence

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProofControllerApi()
licence = 'licence_example' # str | licence (optional)

try:
    # A list of available proofs for a licence
    api_response = api_instance.get_proofs_using_get(licence=licence)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProofControllerApi->get_proofs_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **licence** | **str**| licence | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

