# coding: utf-8

"""
    Api Documentation

    Api Documentation  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class WalletControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def close_wallet_using_delete(self, **kwargs):  # noqa: E501
        """Closes a wallet inside the distributed ledger, this must be done before another operation can be complete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.close_wallet_using_delete(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int wallet_handle:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.close_wallet_using_delete_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.close_wallet_using_delete_with_http_info(**kwargs)  # noqa: E501
            return data

    def close_wallet_using_delete_with_http_info(self, **kwargs):  # noqa: E501
        """Closes a wallet inside the distributed ledger, this must be done before another operation can be complete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.close_wallet_using_delete_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int wallet_handle:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wallet_handle']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method close_wallet_using_delete" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'wallet_handle' in params:
            query_params.append(('walletHandle', params['wallet_handle']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/close-wallet', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_wallet_using_put(self, **kwargs):  # noqa: E501
        """Creates a new wallet inside the distributed ledger  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_wallet_using_put(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id
        :param str key: key
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_wallet_using_put_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_wallet_using_put_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_wallet_using_put_with_http_info(self, **kwargs):  # noqa: E501
        """Creates a new wallet inside the distributed ledger  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_wallet_using_put_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id
        :param str key: key
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_wallet_using_put" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'key' in params:
            query_params.append(('key', params['key']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/create-wallet', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_wallet_with_did_using_put(self, **kwargs):  # noqa: E501
        """Creates a new wallet inside the distributed ledger using a specific DiD  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_wallet_with_did_using_put(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id
        :param str key: key
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_wallet_with_did_using_put_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_wallet_with_did_using_put_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_wallet_with_did_using_put_with_http_info(self, **kwargs):  # noqa: E501
        """Creates a new wallet inside the distributed ledger using a specific DiD  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_wallet_with_did_using_put_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id
        :param str key: key
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_wallet_with_did_using_put" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'key' in params:
            query_params.append(('key', params['key']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/create-wallet-with-did', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_wallet_using_delete(self, **kwargs):  # noqa: E501
        """Deletes a wallet inside the distributed ledger  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_wallet_using_delete(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id
        :param str key: key
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_wallet_using_delete_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_wallet_using_delete_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_wallet_using_delete_with_http_info(self, **kwargs):  # noqa: E501
        """Deletes a wallet inside the distributed ledger  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_wallet_using_delete_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id
        :param str key: key
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_wallet_using_delete" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'key' in params:
            query_params.append(('key', params['key']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/delete-wallet', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def login_using_get(self, **kwargs):  # noqa: E501
        """Logs into a wallet inside the distributed ledger  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.login_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str did: did
        :param str id: id
        :param str key: key
        :param str master_did: masterDid
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.login_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.login_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def login_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Logs into a wallet inside the distributed ledger  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.login_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str did: did
        :param str id: id
        :param str key: key
        :param str master_did: masterDid
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['did', 'id', 'key', 'master_did']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method login_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'did' in params:
            query_params.append(('did', params['did']))  # noqa: E501
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'key' in params:
            query_params.append(('key', params['key']))  # noqa: E501
        if 'master_did' in params:
            query_params.append(('masterDid', params['master_did']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/login', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
