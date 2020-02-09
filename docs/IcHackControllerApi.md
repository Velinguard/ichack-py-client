# swagger_client.IcHackControllerApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_user_id_using_post**](IcHackControllerApi.md#create_new_user_id_using_post) | **POST** /createNewUser | createNewUserID
[**create_new_user_wallet_using_post**](IcHackControllerApi.md#create_new_user_wallet_using_post) | **POST** /create-wallet | createNewUserWallet
[**get_account_id_using_get**](IcHackControllerApi.md#get_account_id_using_get) | **GET** /get-account-id | getAccountID
[**get_event_and_seat_using_get**](IcHackControllerApi.md#get_event_and_seat_using_get) | **GET** /get-event-and-seat-id | getEventAndSeat
[**get_file_using_get**](IcHackControllerApi.md#get_file_using_get) | **GET** /image | getFile
[**issue_airline_ticket_using_post**](IcHackControllerApi.md#issue_airline_ticket_using_post) | **POST** /issue-ticket | issueAirlineTicket
[**verify_proof_from_s3_using_get**](IcHackControllerApi.md#verify_proof_from_s3_using_get) | **GET** /verify | verifyProofFromS3


# **create_new_user_id_using_post**
> EmailInfo create_new_user_id_using_post(_date, cred_def_id=cred_def_id, image=image, issuer_did=issuer_did, issuer_wallet_id=issuer_wallet_id, issuer_wallet_key=issuer_wallet_key, name=name, prover_wallet_id=prover_wallet_id, prover_wallet_key=prover_wallet_key)

createNewUserID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IcHackControllerApi()
_date = '2013-10-20' # date | date
cred_def_id = 'cred_def_id_example' # str | credDefId (optional)
image = '/path/to/file.txt' # file | image (optional)
issuer_did = 'issuer_did_example' # str | issuerDid (optional)
issuer_wallet_id = 'issuer_wallet_id_example' # str | issuerWalletId (optional)
issuer_wallet_key = 'issuer_wallet_key_example' # str | issuerWalletKey (optional)
name = 'name_example' # str | name (optional)
prover_wallet_id = 'prover_wallet_id_example' # str | proverWalletId (optional)
prover_wallet_key = 'prover_wallet_key_example' # str | proverWalletKey (optional)

try:
    # createNewUserID
    api_response = api_instance.create_new_user_id_using_post(_date, cred_def_id=cred_def_id, image=image, issuer_did=issuer_did, issuer_wallet_id=issuer_wallet_id, issuer_wallet_key=issuer_wallet_key, name=name, prover_wallet_id=prover_wallet_id, prover_wallet_key=prover_wallet_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IcHackControllerApi->create_new_user_id_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **date**| date | 
 **cred_def_id** | **str**| credDefId | [optional] 
 **image** | **file**| image | [optional] 
 **issuer_did** | **str**| issuerDid | [optional] 
 **issuer_wallet_id** | **str**| issuerWalletId | [optional] 
 **issuer_wallet_key** | **str**| issuerWalletKey | [optional] 
 **name** | **str**| name | [optional] 
 **prover_wallet_id** | **str**| proverWalletId | [optional] 
 **prover_wallet_key** | **str**| proverWalletKey | [optional] 

### Return type

[**EmailInfo**](EmailInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_new_user_wallet_using_post**
> EmailInfo create_new_user_wallet_using_post(_date, account_id=account_id, image=image, name=name, prover_wallet_id=prover_wallet_id, prover_wallet_key=prover_wallet_key)

createNewUserWallet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IcHackControllerApi()
_date = '2013-10-20' # date | date
account_id = 'account_id_example' # str | accountID (optional)
image = '/path/to/file.txt' # file | image (optional)
name = 'name_example' # str | name (optional)
prover_wallet_id = 'prover_wallet_id_example' # str | proverWalletId (optional)
prover_wallet_key = 'prover_wallet_key_example' # str | proverWalletKey (optional)

try:
    # createNewUserWallet
    api_response = api_instance.create_new_user_wallet_using_post(_date, account_id=account_id, image=image, name=name, prover_wallet_id=prover_wallet_id, prover_wallet_key=prover_wallet_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IcHackControllerApi->create_new_user_wallet_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **date**| date | 
 **account_id** | **str**| accountID | [optional] 
 **image** | **file**| image | [optional] 
 **name** | **str**| name | [optional] 
 **prover_wallet_id** | **str**| proverWalletId | [optional] 
 **prover_wallet_key** | **str**| proverWalletKey | [optional] 

### Return type

[**EmailInfo**](EmailInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_id_using_get**
> str get_account_id_using_get(did=did, id=id, key=key, mid=mid)

getAccountID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IcHackControllerApi()
did = 'did_example' # str | did (optional)
id = 'id_example' # str | id (optional)
key = 'key_example' # str | key (optional)
mid = 'mid_example' # str | mid (optional)

try:
    # getAccountID
    api_response = api_instance.get_account_id_using_get(did=did, id=id, key=key, mid=mid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IcHackControllerApi->get_account_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| did | [optional] 
 **id** | **str**| id | [optional] 
 **key** | **str**| key | [optional] 
 **mid** | **str**| mid | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_and_seat_using_get**
> EventAndSeat get_event_and_seat_using_get(master_secret_id=master_secret_id, prover_did=prover_did, prover_wallet_id=prover_wallet_id, prover_wallet_key=prover_wallet_key)

getEventAndSeat

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IcHackControllerApi()
master_secret_id = 'master_secret_id_example' # str | masterSecretId (optional)
prover_did = 'prover_did_example' # str | proverDID (optional)
prover_wallet_id = 'prover_wallet_id_example' # str | proverWalletId (optional)
prover_wallet_key = 'prover_wallet_key_example' # str | proverWalletKey (optional)

try:
    # getEventAndSeat
    api_response = api_instance.get_event_and_seat_using_get(master_secret_id=master_secret_id, prover_did=prover_did, prover_wallet_id=prover_wallet_id, prover_wallet_key=prover_wallet_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IcHackControllerApi->get_event_and_seat_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **master_secret_id** | **str**| masterSecretId | [optional] 
 **prover_did** | **str**| proverDID | [optional] 
 **prover_wallet_id** | **str**| proverWalletId | [optional] 
 **prover_wallet_key** | **str**| proverWalletKey | [optional] 

### Return type

[**EventAndSeat**](EventAndSeat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_using_get**
> str get_file_using_get()

getFile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IcHackControllerApi()

try:
    # getFile
    api_response = api_instance.get_file_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IcHackControllerApi->get_file_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpg

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_airline_ticket_using_post**
> EmailInfo issue_airline_ticket_using_post(area=area, master_secret_id=master_secret_id, prover_did=prover_did, prover_wallet_id=prover_wallet_id, prover_wallet_key=prover_wallet_key, seat=seat)

issueAirlineTicket

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IcHackControllerApi()
area = 'area_example' # str | area (optional)
master_secret_id = 'master_secret_id_example' # str | masterSecretID (optional)
prover_did = 'prover_did_example' # str | proverDid (optional)
prover_wallet_id = 'prover_wallet_id_example' # str | proverWalletId (optional)
prover_wallet_key = 'prover_wallet_key_example' # str | proverWalletKey (optional)
seat = 'seat_example' # str | seat (optional)

try:
    # issueAirlineTicket
    api_response = api_instance.issue_airline_ticket_using_post(area=area, master_secret_id=master_secret_id, prover_did=prover_did, prover_wallet_id=prover_wallet_id, prover_wallet_key=prover_wallet_key, seat=seat)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IcHackControllerApi->issue_airline_ticket_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area** | **str**| area | [optional] 
 **master_secret_id** | **str**| masterSecretID | [optional] 
 **prover_did** | **str**| proverDid | [optional] 
 **prover_wallet_id** | **str**| proverWalletId | [optional] 
 **prover_wallet_key** | **str**| proverWalletKey | [optional] 
 **seat** | **str**| seat | [optional] 

### Return type

[**EmailInfo**](EmailInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_proof_from_s3_using_get**
> ImageName verify_proof_from_s3_using_get(bucket_name=bucket_name, object_name=object_name, proof=proof, verifier_did=verifier_did, verifier_wallet_id=verifier_wallet_id, verifier_wallet_key=verifier_wallet_key)

verifyProofFromS3

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IcHackControllerApi()
bucket_name = 'bucket_name_example' # str | bucketName (optional)
object_name = 'object_name_example' # str | objectName (optional)
proof = 'proof_example' # str | proof (optional)
verifier_did = 'verifier_did_example' # str | verifierDid (optional)
verifier_wallet_id = 'verifier_wallet_id_example' # str | verifierWalletId (optional)
verifier_wallet_key = 'verifier_wallet_key_example' # str | verifierWalletKey (optional)

try:
    # verifyProofFromS3
    api_response = api_instance.verify_proof_from_s3_using_get(bucket_name=bucket_name, object_name=object_name, proof=proof, verifier_did=verifier_did, verifier_wallet_id=verifier_wallet_id, verifier_wallet_key=verifier_wallet_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IcHackControllerApi->verify_proof_from_s3_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_name** | **str**| bucketName | [optional] 
 **object_name** | **str**| objectName | [optional] 
 **proof** | **str**| proof | [optional] 
 **verifier_did** | **str**| verifierDid | [optional] 
 **verifier_wallet_id** | **str**| verifierWalletId | [optional] 
 **verifier_wallet_key** | **str**| verifierWalletKey | [optional] 

### Return type

[**ImageName**](ImageName.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpg

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

