# swagger_client.VerifierControllerApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verify_proof_from_s3_using_get1**](VerifierControllerApi.md#verify_proof_from_s3_using_get1) | **GET** /prove-s3 | Verifies a proof for the verifier using a proof stored on the File System
[**verify_proof_using_get**](VerifierControllerApi.md#verify_proof_using_get) | **GET** /prove | Verifies a proof for the verifier


# **verify_proof_from_s3_using_get1**
> object verify_proof_from_s3_using_get1(bucket_name=bucket_name, name=name, object_name=object_name, proof=proof, verifier_did=verifier_did, verifier_wallet_id=verifier_wallet_id, verifier_wallet_key=verifier_wallet_key)

Verifies a proof for the verifier using a proof stored on the File System

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VerifierControllerApi()
bucket_name = 'bucket_name_example' # str | bucketName (optional)
name = 'name_example' # str | name (optional)
object_name = 'object_name_example' # str | objectName (optional)
proof = 'proof_example' # str | proof (optional)
verifier_did = 'verifier_did_example' # str | verifierDid (optional)
verifier_wallet_id = 'verifier_wallet_id_example' # str | verifierWalletId (optional)
verifier_wallet_key = 'verifier_wallet_key_example' # str | verifierWalletKey (optional)

try:
    # Verifies a proof for the verifier using a proof stored on the File System
    api_response = api_instance.verify_proof_from_s3_using_get1(bucket_name=bucket_name, name=name, object_name=object_name, proof=proof, verifier_did=verifier_did, verifier_wallet_id=verifier_wallet_id, verifier_wallet_key=verifier_wallet_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerifierControllerApi->verify_proof_from_s3_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_name** | **str**| bucketName | [optional] 
 **name** | **str**| name | [optional] 
 **object_name** | **str**| objectName | [optional] 
 **proof** | **str**| proof | [optional] 
 **verifier_did** | **str**| verifierDid | [optional] 
 **verifier_wallet_id** | **str**| verifierWalletId | [optional] 
 **verifier_wallet_key** | **str**| verifierWalletKey | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_proof_using_get**
> object verify_proof_using_get(cred_def_id=cred_def_id, cred_def_id2=cred_def_id2, cred_def_json=cred_def_json, cred_defs=cred_defs, name=name, proof_json=proof_json, proof_request_json=proof_request_json, schema_id=schema_id, verifier_did=verifier_did, verifier_wallet_id=verifier_wallet_id, verifier_wallet_key=verifier_wallet_key)

Verifies a proof for the verifier

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VerifierControllerApi()
cred_def_id = 'cred_def_id_example' # str |  (optional)
cred_def_id2 = 'cred_def_id_example' # str | credDefId (optional)
cred_def_json = 'cred_def_json_example' # str |  (optional)
cred_defs = 'cred_defs_example' # str |  (optional)
name = 'name_example' # str | name (optional)
proof_json = 'proof_json_example' # str | proofJson (optional)
proof_request_json = 'proof_request_json_example' # str | proofRequestJson (optional)
schema_id = 'schema_id_example' # str | schemaId (optional)
verifier_did = 'verifier_did_example' # str | verifierDid (optional)
verifier_wallet_id = 'verifier_wallet_id_example' # str | verifierWalletId (optional)
verifier_wallet_key = 'verifier_wallet_key_example' # str | verifierWalletKey (optional)

try:
    # Verifies a proof for the verifier
    api_response = api_instance.verify_proof_using_get(cred_def_id=cred_def_id, cred_def_id2=cred_def_id2, cred_def_json=cred_def_json, cred_defs=cred_defs, name=name, proof_json=proof_json, proof_request_json=proof_request_json, schema_id=schema_id, verifier_did=verifier_did, verifier_wallet_id=verifier_wallet_id, verifier_wallet_key=verifier_wallet_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerifierControllerApi->verify_proof_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_def_id** | **str**|  | [optional] 
 **cred_def_id2** | **str**| credDefId | [optional] 
 **cred_def_json** | **str**|  | [optional] 
 **cred_defs** | **str**|  | [optional] 
 **name** | **str**| name | [optional] 
 **proof_json** | **str**| proofJson | [optional] 
 **proof_request_json** | **str**| proofRequestJson | [optional] 
 **schema_id** | **str**| schemaId | [optional] 
 **verifier_did** | **str**| verifierDid | [optional] 
 **verifier_wallet_id** | **str**| verifierWalletId | [optional] 
 **verifier_wallet_key** | **str**| verifierWalletKey | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

