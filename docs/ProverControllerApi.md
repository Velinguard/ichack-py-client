# swagger_client.ProverControllerApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**prover_get_default_credentials_using_get**](ProverControllerApi.md#prover_get_default_credentials_using_get) | **GET** /credentials-for-default-proof | Creates a proof request for the prover stored on the file system S3
[**prover_get_proof_credentials_using_get**](ProverControllerApi.md#prover_get_proof_credentials_using_get) | **GET** /credentials-for-proof | proverGetProofCredentials


# **prover_get_default_credentials_using_get**
> str prover_get_default_credentials_using_get(master_secret_id=master_secret_id, proof=proof, prover_did=prover_did, prover_wallet_id=prover_wallet_id, prover_wallet_key=prover_wallet_key)

Creates a proof request for the prover stored on the file system S3

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProverControllerApi()
master_secret_id = 'master_secret_id_example' # str | masterSecretId (optional)
proof = 'proof_example' # str | proof (optional)
prover_did = 'prover_did_example' # str | proverDID (optional)
prover_wallet_id = 'prover_wallet_id_example' # str | proverWalletID (optional)
prover_wallet_key = 'prover_wallet_key_example' # str | proverWalletKey (optional)

try:
    # Creates a proof request for the prover stored on the file system S3
    api_response = api_instance.prover_get_default_credentials_using_get(master_secret_id=master_secret_id, proof=proof, prover_did=prover_did, prover_wallet_id=prover_wallet_id, prover_wallet_key=prover_wallet_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProverControllerApi->prover_get_default_credentials_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **master_secret_id** | **str**| masterSecretId | [optional] 
 **proof** | **str**| proof | [optional] 
 **prover_did** | **str**| proverDID | [optional] 
 **prover_wallet_id** | **str**| proverWalletID | [optional] 
 **prover_wallet_key** | **str**| proverWalletKey | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prover_get_proof_credentials_using_get**
> str prover_get_proof_credentials_using_get(cred_def_id=cred_def_id, master_secret_id=master_secret_id, proof_request_json=proof_request_json, prover_did=prover_did, prover_wallet_id=prover_wallet_id, prover_wallet_key=prover_wallet_key, schema_id=schema_id)

proverGetProofCredentials

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProverControllerApi()
cred_def_id = 'cred_def_id_example' # str | credDefId (optional)
master_secret_id = 'master_secret_id_example' # str | masterSecretId (optional)
proof_request_json = 'proof_request_json_example' # str | proofRequestJson (optional)
prover_did = 'prover_did_example' # str | proverDID (optional)
prover_wallet_id = 'prover_wallet_id_example' # str | proverWalletID (optional)
prover_wallet_key = 'prover_wallet_key_example' # str | proverWalletKey (optional)
schema_id = 'schema_id_example' # str | schemaId (optional)

try:
    # proverGetProofCredentials
    api_response = api_instance.prover_get_proof_credentials_using_get(cred_def_id=cred_def_id, master_secret_id=master_secret_id, proof_request_json=proof_request_json, prover_did=prover_did, prover_wallet_id=prover_wallet_id, prover_wallet_key=prover_wallet_key, schema_id=schema_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProverControllerApi->prover_get_proof_credentials_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_def_id** | **str**| credDefId | [optional] 
 **master_secret_id** | **str**| masterSecretId | [optional] 
 **proof_request_json** | **str**| proofRequestJson | [optional] 
 **prover_did** | **str**| proverDID | [optional] 
 **prover_wallet_id** | **str**| proverWalletID | [optional] 
 **prover_wallet_key** | **str**| proverWalletKey | [optional] 
 **schema_id** | **str**| schemaId | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

