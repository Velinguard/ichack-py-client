# swagger_client.MasterControllerApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cred_schema_using_put**](MasterControllerApi.md#create_cred_schema_using_put) | **PUT** /create-credential-schema | Creates a new credential schema for the Issuer
[**create_credential_definition_using_put**](MasterControllerApi.md#create_credential_definition_using_put) | **PUT** /create-credential-definition | Create a credential definition for the issuer to reference the schema
[**create_issuer_using_put**](MasterControllerApi.md#create_issuer_using_put) | **PUT** /create-issuer | Creates a new issuer for the given ID and Key pair


# **create_cred_schema_using_put**
> str create_cred_schema_using_put(default_steward_did=default_steward_did, licence=licence, wallet_id=wallet_id, wallet_key=wallet_key)

Creates a new credential schema for the Issuer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MasterControllerApi()
default_steward_did = 'default_steward_did_example' # str | defaultStewardDid (optional)
licence = 'licence_example' # str | licence (optional)
wallet_id = 'wallet_id_example' # str | walletId (optional)
wallet_key = 'wallet_key_example' # str | walletKey (optional)

try:
    # Creates a new credential schema for the Issuer
    api_response = api_instance.create_cred_schema_using_put(default_steward_did=default_steward_did, licence=licence, wallet_id=wallet_id, wallet_key=wallet_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasterControllerApi->create_cred_schema_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **default_steward_did** | **str**| defaultStewardDid | [optional] 
 **licence** | **str**| licence | [optional] 
 **wallet_id** | **str**| walletId | [optional] 
 **wallet_key** | **str**| walletKey | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_credential_definition_using_put**
> str create_credential_definition_using_put(person_did=person_did, schema_id=schema_id, wallet_id=wallet_id, wallet_key=wallet_key)

Create a credential definition for the issuer to reference the schema

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MasterControllerApi()
person_did = 'person_did_example' # str | personDid (optional)
schema_id = 'schema_id_example' # str | schemaId (optional)
wallet_id = 'wallet_id_example' # str | walletId (optional)
wallet_key = 'wallet_key_example' # str | walletKey (optional)

try:
    # Create a credential definition for the issuer to reference the schema
    api_response = api_instance.create_credential_definition_using_put(person_did=person_did, schema_id=schema_id, wallet_id=wallet_id, wallet_key=wallet_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasterControllerApi->create_credential_definition_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_did** | **str**| personDid | [optional] 
 **schema_id** | **str**| schemaId | [optional] 
 **wallet_id** | **str**| walletId | [optional] 
 **wallet_key** | **str**| walletKey | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_issuer_using_put**
> str create_issuer_using_put(wallet_id=wallet_id, wallet_key=wallet_key)

Creates a new issuer for the given ID and Key pair

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MasterControllerApi()
wallet_id = 'wallet_id_example' # str | walletId (optional)
wallet_key = 'wallet_key_example' # str | walletKey (optional)

try:
    # Creates a new issuer for the given ID and Key pair
    api_response = api_instance.create_issuer_using_put(wallet_id=wallet_id, wallet_key=wallet_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasterControllerApi->create_issuer_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| walletId | [optional] 
 **wallet_key** | **str**| walletKey | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

