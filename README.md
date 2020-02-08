# swagger-client
Api Documentation

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BasicErrorControllerApi(swagger_client.ApiClient(configuration))

try:
    # errorHtml
    api_response = api_instance.error_html_using_delete()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasicErrorControllerApi->error_html_using_delete: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost:8080*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BasicErrorControllerApi* | [**error_html_using_delete**](docs/BasicErrorControllerApi.md#error_html_using_delete) | **DELETE** /error | errorHtml
*BasicErrorControllerApi* | [**error_html_using_get**](docs/BasicErrorControllerApi.md#error_html_using_get) | **GET** /error | errorHtml
*BasicErrorControllerApi* | [**error_html_using_head**](docs/BasicErrorControllerApi.md#error_html_using_head) | **HEAD** /error | errorHtml
*BasicErrorControllerApi* | [**error_html_using_options**](docs/BasicErrorControllerApi.md#error_html_using_options) | **OPTIONS** /error | errorHtml
*BasicErrorControllerApi* | [**error_html_using_patch**](docs/BasicErrorControllerApi.md#error_html_using_patch) | **PATCH** /error | errorHtml
*BasicErrorControllerApi* | [**error_html_using_post**](docs/BasicErrorControllerApi.md#error_html_using_post) | **POST** /error | errorHtml
*BasicErrorControllerApi* | [**error_html_using_put**](docs/BasicErrorControllerApi.md#error_html_using_put) | **PUT** /error | errorHtml
*IcHackControllerApi* | [**create_new_user_id_using_post**](docs/IcHackControllerApi.md#create_new_user_id_using_post) | **POST** /createNewUser | createNewUserID
*IcHackControllerApi* | [**create_new_user_wallet_using_post**](docs/IcHackControllerApi.md#create_new_user_wallet_using_post) | **POST** /create-wallet | createNewUserWallet
*IcHackControllerApi* | [**get_account_id_using_get**](docs/IcHackControllerApi.md#get_account_id_using_get) | **GET** /get-account-id | getAccountID
*IcHackControllerApi* | [**get_file_using_get**](docs/IcHackControllerApi.md#get_file_using_get) | **GET** /image | getFile
*IcHackControllerApi* | [**issue_ticket_using_post**](docs/IcHackControllerApi.md#issue_ticket_using_post) | **POST** /issue-ticket | issueTicket
*IcHackControllerApi* | [**verify_proof_from_s3_using_get**](docs/IcHackControllerApi.md#verify_proof_from_s3_using_get) | **GET** /verify | verifyProofFromS3
*IssuerControllerApi* | [**get_credential_definition_using_put**](docs/IssuerControllerApi.md#get_credential_definition_using_put) | **PUT** /get-credential-definition | getCredentialDefinition
*IssuerControllerApi* | [**issuer_create_credentials_using_put**](docs/IssuerControllerApi.md#issuer_create_credentials_using_put) | **PUT** /create | Issues a Driving Licence to a prover
*IssuerControllerApi* | [**issuer_create_ticket_credentials_using_put**](docs/IssuerControllerApi.md#issuer_create_ticket_credentials_using_put) | **PUT** /create-ticket | Issues a ticket to a prover
*IssuerControllerApi* | [**issuer_email_created_credentials_using_put**](docs/IssuerControllerApi.md#issuer_email_created_credentials_using_put) | **PUT** /create-email | Issues a Driving Licence to a prover, emailing the response
*IssuerControllerApi* | [**issuer_email_created_ticket_credentials_using_put**](docs/IssuerControllerApi.md#issuer_email_created_ticket_credentials_using_put) | **PUT** /create-email-ticket | Issues a ticket to a prover, emailing the response
*MasterControllerApi* | [**create_cred_schema_using_put**](docs/MasterControllerApi.md#create_cred_schema_using_put) | **PUT** /create-credential-schema | Creates a new credential schema for the Issuer
*MasterControllerApi* | [**create_credential_definition_using_put**](docs/MasterControllerApi.md#create_credential_definition_using_put) | **PUT** /create-credential-definition | Create a credential definition for the issuer to reference the schema
*MasterControllerApi* | [**create_issuer_using_put**](docs/MasterControllerApi.md#create_issuer_using_put) | **PUT** /create-issuer | Creates a new issuer for the given ID and Key pair
*ProofControllerApi* | [**get_licences_using_get**](docs/ProofControllerApi.md#get_licences_using_get) | **GET** /get-licence-type | A list of licences available
*ProofControllerApi* | [**get_proof_json_using_get**](docs/ProofControllerApi.md#get_proof_json_using_get) | **GET** /get-proof | A proof json for a given proof
*ProofControllerApi* | [**get_proof_request_using_get**](docs/ProofControllerApi.md#get_proof_request_using_get) | **GET** /get-proof-request | getProofRequest
*ProofControllerApi* | [**get_proofs_using_get**](docs/ProofControllerApi.md#get_proofs_using_get) | **GET** /get-proofs | A list of available proofs for a licence
*ProverControllerApi* | [**prover_get_default_credentials_using_get**](docs/ProverControllerApi.md#prover_get_default_credentials_using_get) | **GET** /credentials-for-default-proof | Creates a proof request for the prover stored on the file system S3
*ProverControllerApi* | [**prover_get_proof_credentials_using_get**](docs/ProverControllerApi.md#prover_get_proof_credentials_using_get) | **GET** /credentials-for-proof | proverGetProofCredentials
*VerifierControllerApi* | [**verify_proof_from_s3_using_get1**](docs/VerifierControllerApi.md#verify_proof_from_s3_using_get1) | **GET** /prove-s3 | Verifies a proof for the verifier using a proof stored on the File System
*VerifierControllerApi* | [**verify_proof_using_get**](docs/VerifierControllerApi.md#verify_proof_using_get) | **GET** /prove | Verifies a proof for the verifier
*WalletControllerApi* | [**close_wallet_using_delete**](docs/WalletControllerApi.md#close_wallet_using_delete) | **DELETE** /close-wallet | Closes a wallet inside the distributed ledger, this must be done before another operation can be complete
*WalletControllerApi* | [**create_wallet_using_put**](docs/WalletControllerApi.md#create_wallet_using_put) | **PUT** /create-wallet | Creates a new wallet inside the distributed ledger
*WalletControllerApi* | [**create_wallet_with_did_using_put**](docs/WalletControllerApi.md#create_wallet_with_did_using_put) | **PUT** /create-wallet-with-did | Creates a new wallet inside the distributed ledger using a specific DiD
*WalletControllerApi* | [**delete_wallet_using_delete**](docs/WalletControllerApi.md#delete_wallet_using_delete) | **DELETE** /delete-wallet | Deletes a wallet inside the distributed ledger
*WalletControllerApi* | [**login_using_get**](docs/WalletControllerApi.md#login_using_get) | **GET** /login | Logs into a wallet inside the distributed ledger


## Documentation For Models

 - [CredentialDefinition](docs/CredentialDefinition.md)
 - [EmailInfo](docs/EmailInfo.md)
 - [ImageName](docs/ImageName.md)
 - [ModelAndView](docs/ModelAndView.md)
 - [View](docs/View.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



