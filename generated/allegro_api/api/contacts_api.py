# coding: utf-8

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    The version of the OpenAPI document: 2020.03.12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from allegro_api.api_client import ApiClient
from allegro_api.exceptions import (
    ApiTypeError,
    ApiValueError
)


class ContactsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_contact_using_post(self, contact_request, **kwargs):  # noqa: E501
        """Create a new contact  # noqa: E501

        Use this resource to create a new contact. <a href=\"../../news/2018-01-17-news_zarzadzanie_kontaktami/#1\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_contact_using_post(contact_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param ContactRequest contact_request: New contact (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ContactResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_contact_using_post_with_http_info(contact_request, **kwargs)  # noqa: E501

    def create_contact_using_post_with_http_info(self, contact_request, **kwargs):  # noqa: E501
        """Create a new contact  # noqa: E501

        Use this resource to create a new contact. <a href=\"../../news/2018-01-17-news_zarzadzanie_kontaktami/#1\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_contact_using_post_with_http_info(contact_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param ContactRequest contact_request: New contact (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ContactResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['contact_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_contact_using_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'contact_request' is set
        if self.api_client.client_side_validation and ('contact_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['contact_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `contact_request` when calling `create_contact_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'contact_request' in local_var_params:
            body_params = local_var_params['contact_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.allegro.public.v1+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/vnd.allegro.public.v1+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer-token-for-user']  # noqa: E501

        return self.api_client.call_api(
            '/sale/offer-contacts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ContactResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_contact_using_get(self, id, **kwargs):  # noqa: E501
        """Get contact details  # noqa: E501

        Use this resource to get contact details. <a href=\"../../news/2018-01-17-news_zarzadzanie_kontaktami/#3\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_contact_using_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Contact identifier. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ContactResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_contact_using_get_with_http_info(id, **kwargs)  # noqa: E501

    def get_contact_using_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get contact details  # noqa: E501

        Use this resource to get contact details. <a href=\"../../news/2018-01-17-news_zarzadzanie_kontaktami/#3\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_contact_using_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Contact identifier. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ContactResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_contact_using_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `get_contact_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.allegro.public.v1+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer-token-for-user']  # noqa: E501

        return self.api_client.call_api(
            '/sale/offer-contacts/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ContactResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_list_of_contacts_using_get(self, seller_id, **kwargs):  # noqa: E501
        """Get the user's contacts  # noqa: E501

        Use this resource to get details of many contacts. <a href=\"../../news/2018-01-17-news_zarzadzanie_kontaktami/#4\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_list_of_contacts_using_get(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str seller_id: Contacts owner identifier. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ContactResponseList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_list_of_contacts_using_get_with_http_info(seller_id, **kwargs)  # noqa: E501

    def get_list_of_contacts_using_get_with_http_info(self, seller_id, **kwargs):  # noqa: E501
        """Get the user's contacts  # noqa: E501

        Use this resource to get details of many contacts. <a href=\"../../news/2018-01-17-news_zarzadzanie_kontaktami/#4\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_list_of_contacts_using_get_with_http_info(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str seller_id: Contacts owner identifier. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ContactResponseList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['seller_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_list_of_contacts_using_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'seller_id' is set
        if self.api_client.client_side_validation and ('seller_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['seller_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `seller_id` when calling `get_list_of_contacts_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'seller_id' in local_var_params and local_var_params['seller_id'] is not None:  # noqa: E501
            query_params.append(('seller.id', local_var_params['seller_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.allegro.public.v1+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer-token-for-user']  # noqa: E501

        return self.api_client.call_api(
            '/sale/offer-contacts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ContactResponseList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_contact_using_put(self, id, contact_request, **kwargs):  # noqa: E501
        """Modify contact details  # noqa: E501

        Use this resource to modify contact details. <a href=\"../../news/2018-01-17-news_zarzadzanie_kontaktami/#2\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_contact_using_put(id, contact_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Contact identifier. (required)
        :param ContactRequest contact_request: Contact (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ContactResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.modify_contact_using_put_with_http_info(id, contact_request, **kwargs)  # noqa: E501

    def modify_contact_using_put_with_http_info(self, id, contact_request, **kwargs):  # noqa: E501
        """Modify contact details  # noqa: E501

        Use this resource to modify contact details. <a href=\"../../news/2018-01-17-news_zarzadzanie_kontaktami/#2\" target=\"_blank\">Read more</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_contact_using_put_with_http_info(id, contact_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Contact identifier. (required)
        :param ContactRequest contact_request: Contact (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ContactResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'contact_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_contact_using_put" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `modify_contact_using_put`")  # noqa: E501
        # verify the required parameter 'contact_request' is set
        if self.api_client.client_side_validation and ('contact_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['contact_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `contact_request` when calling `modify_contact_using_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'contact_request' in local_var_params:
            body_params = local_var_params['contact_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.allegro.public.v1+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/vnd.allegro.public.v1+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer-token-for-user']  # noqa: E501

        return self.api_client.call_api(
            '/sale/offer-contacts/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ContactResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
