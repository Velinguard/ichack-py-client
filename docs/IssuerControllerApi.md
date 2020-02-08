# swagger_client.IssuerControllerApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_credential_definition_using_put**](IssuerControllerApi.md#get_credential_definition_using_put) | **PUT** /get-credential-definition | getCredentialDefinition
[**issuer_create_credentials_using_put**](IssuerControllerApi.md#issuer_create_credentials_using_put) | **PUT** /create | Issues a Driving Licence to a prover
[**issuer_create_ticket_credentials_using_put**](IssuerControllerApi.md#issuer_create_ticket_credentials_using_put) | **PUT** /create-ticket | Issues a ticket to a prover
[**issuer_email_created_credentials_using_put**](IssuerControllerApi.md#issuer_email_created_credentials_using_put) | **PUT** /create-email | Issues a Driving Licence to a prover, emailing the response
[**issuer_email_created_ticket_credentials_using_put**](IssuerControllerApi.md#issuer_email_created_ticket_credentials_using_put) | **PUT** /create-email-ticket | Issues a ticket to a prover, emailing the response


# **get_credential_definition_using_put**
> CredentialDefinition get_credential_definition_using_put(cred_def_id=cred_def_id, indy_wallet_wallet_handle=indy_wallet_wallet_handle, master_secret_id=master_secret_id, name=name, person_did=person_did)

getCredentialDefinition

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssuerControllerApi()
cred_def_id = 'cred_def_id_example' # str | credDefId (optional)
indy_wallet_wallet_handle = 56 # int |  (optional)
master_secret_id = 'master_secret_id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
person_did = 'person_did_example' # str |  (optional)

try:
    # getCredentialDefinition
    api_response = api_instance.get_credential_definition_using_put(cred_def_id=cred_def_id, indy_wallet_wallet_handle=indy_wallet_wallet_handle, master_secret_id=master_secret_id, name=name, person_did=person_did)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuerControllerApi->get_credential_definition_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_def_id** | **str**| credDefId | [optional] 
 **indy_wallet_wallet_handle** | **int**|  | [optional] 
 **master_secret_id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **person_did** | **str**|  | [optional] 

### Return type

[**CredentialDefinition**](CredentialDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issuer_create_credentials_using_put**
> object issuer_create_credentials_using_put(cred_def_id=cred_def_id, date_of_birth=date_of_birth, issuer_did=issuer_did, issuer_wallet_id=issuer_wallet_id, issuer_wallet_key=issuer_wallet_key, licence_level=licence_level, name=name, prover_did=prover_did, prover_wallet_id=prover_wallet_id, prover_wallet_key=prover_wallet_key)

Issues a Driving Licence to a prover

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssuerControllerApi()
cred_def_id = 'cred_def_id_example' # str | credDefId (optional)
date_of_birth = 'date_of_birth_example' # str | dateOfBirth (optional)
issuer_did = 'issuer_did_example' # str | issuerDid (optional)
issuer_wallet_id = 'issuer_wallet_id_example' # str | issuerWalletId (optional)
issuer_wallet_key = 'issuer_wallet_key_example' # str | issuerWalletKey (optional)
licence_level = 'licence_level_example' # str | licenceLevel (optional)
name = 'name_example' # str | name (optional)
prover_did = 'prover_did_example' # str | proverDid (optional)
prover_wallet_id = 'prover_wallet_id_example' # str | proverWalletId (optional)
prover_wallet_key = 'prover_wallet_key_example' # str | proverWalletKey (optional)

try:
    # Issues a Driving Licence to a prover
    api_response = api_instance.issuer_create_credentials_using_put(cred_def_id=cred_def_id, date_of_birth=date_of_birth, issuer_did=issuer_did, issuer_wallet_id=issuer_wallet_id, issuer_wallet_key=issuer_wallet_key, licence_level=licence_level, name=name, prover_did=prover_did, prover_wallet_id=prover_wallet_id, prover_wallet_key=prover_wallet_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuerControllerApi->issuer_create_credentials_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_def_id** | **str**| credDefId | [optional] 
 **date_of_birth** | **str**| dateOfBirth | [optional] 
 **issuer_did** | **str**| issuerDid | [optional] 
 **issuer_wallet_id** | **str**| issuerWalletId | [optional] 
 **issuer_wallet_key** | **str**| issuerWalletKey | [optional] 
 **licence_level** | **str**| licenceLevel | [optional] 
 **name** | **str**| name | [optional] 
 **prover_did** | **str**| proverDid | [optional] 
 **prover_wallet_id** | **str**| proverWalletId | [optional] 
 **prover_wallet_key** | **str**| proverWalletKey | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issuer_create_ticket_credentials_using_put**
> object issuer_create_ticket_credentials_using_put(cred_def_id=cred_def_id, issuer_did=issuer_did, issuer_wallet_id=issuer_wallet_id, issuer_wallet_key=issuer_wallet_key, name=name, prover_did=prover_did, prover_wallet_id=prover_wallet_id, prover_wallet_key=prover_wallet_key, ticket_level=ticket_level)

Issues a ticket to a prover

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssuerControllerApi()
cred_def_id = 'cred_def_id_example' # str | credDefId (optional)
issuer_did = 'issuer_did_example' # str | issuerDid (optional)
issuer_wallet_id = 'issuer_wallet_id_example' # str | issuerWalletId (optional)
issuer_wallet_key = 'issuer_wallet_key_example' # str | issuerWalletKey (optional)
name = 'name_example' # str | name (optional)
prover_did = 'prover_did_example' # str | proverDid (optional)
prover_wallet_id = 'prover_wallet_id_example' # str | proverWalletId (optional)
prover_wallet_key = 'prover_wallet_key_example' # str | proverWalletKey (optional)
ticket_level = 'ticket_level_example' # str | ticketLevel (optional)

try:
    # Issues a ticket to a prover
    api_response = api_instance.issuer_create_ticket_credentials_using_put(cred_def_id=cred_def_id, issuer_did=issuer_did, issuer_wallet_id=issuer_wallet_id, issuer_wallet_key=issuer_wallet_key, name=name, prover_did=prover_did, prover_wallet_id=prover_wallet_id, prover_wallet_key=prover_wallet_key, ticket_level=ticket_level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuerControllerApi->issuer_create_ticket_credentials_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_def_id** | **str**| credDefId | [optional] 
 **issuer_did** | **str**| issuerDid | [optional] 
 **issuer_wallet_id** | **str**| issuerWalletId | [optional] 
 **issuer_wallet_key** | **str**| issuerWalletKey | [optional] 
 **name** | **str**| name | [optional] 
 **prover_did** | **str**| proverDid | [optional] 
 **prover_wallet_id** | **str**| proverWalletId | [optional] 
 **prover_wallet_key** | **str**| proverWalletKey | [optional] 
 **ticket_level** | **str**| ticketLevel | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issuer_email_created_credentials_using_put**
> str issuer_email_created_credentials_using_put(cred_def_id=cred_def_id, date_of_birth=date_of_birth, email=email, issuer_did=issuer_did, issuer_wallet_id=issuer_wallet_id, issuer_wallet_key=issuer_wallet_key, licence_level=licence_level, name=name, prover_did=prover_did, prover_wallet_id=prover_wallet_id, prover_wallet_key=prover_wallet_key)

Issues a Driving Licence to a prover, emailing the response

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssuerControllerApi()
cred_def_id = 'cred_def_id_example' # str | credDefId (optional)
date_of_birth = 'date_of_birth_example' # str | dateOfBirth (optional)
email = 'email_example' # str | email (optional)
issuer_did = 'issuer_did_example' # str | issuerDid (optional)
issuer_wallet_id = 'issuer_wallet_id_example' # str | issuerWalletId (optional)
issuer_wallet_key = 'issuer_wallet_key_example' # str | issuerWalletKey (optional)
licence_level = 'licence_level_example' # str | licenceLevel (optional)
name = 'name_example' # str | name (optional)
prover_did = 'prover_did_example' # str | proverDid (optional)
prover_wallet_id = 'prover_wallet_id_example' # str | proverWalletId (optional)
prover_wallet_key = 'prover_wallet_key_example' # str | proverWalletKey (optional)

try:
    # Issues a Driving Licence to a prover, emailing the response
    api_response = api_instance.issuer_email_created_credentials_using_put(cred_def_id=cred_def_id, date_of_birth=date_of_birth, email=email, issuer_did=issuer_did, issuer_wallet_id=issuer_wallet_id, issuer_wallet_key=issuer_wallet_key, licence_level=licence_level, name=name, prover_did=prover_did, prover_wallet_id=prover_wallet_id, prover_wallet_key=prover_wallet_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuerControllerApi->issuer_email_created_credentials_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_def_id** | **str**| credDefId | [optional] 
 **date_of_birth** | **str**| dateOfBirth | [optional] 
 **email** | **str**| email | [optional] 
 **issuer_did** | **str**| issuerDid | [optional] 
 **issuer_wallet_id** | **str**| issuerWalletId | [optional] 
 **issuer_wallet_key** | **str**| issuerWalletKey | [optional] 
 **licence_level** | **str**| licenceLevel | [optional] 
 **name** | **str**| name | [optional] 
 **prover_did** | **str**| proverDid | [optional] 
 **prover_wallet_id** | **str**| proverWalletId | [optional] 
 **prover_wallet_key** | **str**| proverWalletKey | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issuer_email_created_ticket_credentials_using_put**
> str issuer_email_created_ticket_credentials_using_put(cred_def_id=cred_def_id, email=email, issuer_did=issuer_did, issuer_wallet_id=issuer_wallet_id, issuer_wallet_key=issuer_wallet_key, name=name, prover_did=prover_did, prover_wallet_id=prover_wallet_id, prover_wallet_key=prover_wallet_key, ticket_level=ticket_level)

Issues a ticket to a prover, emailing the response

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssuerControllerApi()
cred_def_id = 'cred_def_id_example' # str | credDefId (optional)
email = 'email_example' # str | email (optional)
issuer_did = 'issuer_did_example' # str | issuerDid (optional)
issuer_wallet_id = 'issuer_wallet_id_example' # str | issuerWalletId (optional)
issuer_wallet_key = 'issuer_wallet_key_example' # str | issuerWalletKey (optional)
name = 'name_example' # str | name (optional)
prover_did = 'prover_did_example' # str | proverDid (optional)
prover_wallet_id = 'prover_wallet_id_example' # str | proverWalletId (optional)
prover_wallet_key = 'prover_wallet_key_example' # str | proverWalletKey (optional)
ticket_level = 'ticket_level_example' # str | ticketLevel (optional)

try:
    # Issues a ticket to a prover, emailing the response
    api_response = api_instance.issuer_email_created_ticket_credentials_using_put(cred_def_id=cred_def_id, email=email, issuer_did=issuer_did, issuer_wallet_id=issuer_wallet_id, issuer_wallet_key=issuer_wallet_key, name=name, prover_did=prover_did, prover_wallet_id=prover_wallet_id, prover_wallet_key=prover_wallet_key, ticket_level=ticket_level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuerControllerApi->issuer_email_created_ticket_credentials_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_def_id** | **str**| credDefId | [optional] 
 **email** | **str**| email | [optional] 
 **issuer_did** | **str**| issuerDid | [optional] 
 **issuer_wallet_id** | **str**| issuerWalletId | [optional] 
 **issuer_wallet_key** | **str**| issuerWalletKey | [optional] 
 **name** | **str**| name | [optional] 
 **prover_did** | **str**| proverDid | [optional] 
 **prover_wallet_id** | **str**| proverWalletId | [optional] 
 **prover_wallet_key** | **str**| proverWalletKey | [optional] 
 **ticket_level** | **str**| ticketLevel | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

