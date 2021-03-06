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


class PaymentsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_payment_id_mapping(self, **kwargs):  # noqa: E501
        """Mapping of payment identifiers  # noqa: E501

        Use this endpoint to get payment identifiers compatible with RestAPI and WebAPI. Querying is allowed only by paymentId or transactionId. Identifiers are returned for payments created in last 3 months.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payment_id_mapping(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_id: Payment identifier.
        :param str transaction_id: Transaction identifier.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PaymentIdMapping
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_payment_id_mapping_with_http_info(**kwargs)  # noqa: E501

    def get_payment_id_mapping_with_http_info(self, **kwargs):  # noqa: E501
        """Mapping of payment identifiers  # noqa: E501

        Use this endpoint to get payment identifiers compatible with RestAPI and WebAPI. Querying is allowed only by paymentId or transactionId. Identifiers are returned for payments created in last 3 months.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payment_id_mapping_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_id: Payment identifier.
        :param str transaction_id: Transaction identifier.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PaymentIdMapping, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payment_id', 'transaction_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payment_id_mapping" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'payment_id' in local_var_params and local_var_params['payment_id'] is not None:  # noqa: E501
            query_params.append(('paymentId', local_var_params['payment_id']))  # noqa: E501
        if 'transaction_id' in local_var_params and local_var_params['transaction_id'] is not None:  # noqa: E501
            query_params.append(('transactionId', local_var_params['transaction_id']))  # noqa: E501

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
            '/payments/payment-id-mappings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaymentIdMapping',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_payments_operation_history(self, **kwargs):  # noqa: E501
        """Payment operations history  # noqa: E501

        Use this endpoint to get the list of the seller's payment operations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payments_operation_history(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str wallet_type: Type of the wallet: * AVAILABLE - operations available for payout. * WAITING - operations temporarily suspended for payout.
        :param str wallet_payment_operator: Payment operator: * PAYU - operations processed by PAYU operator. * P24 - operations processed by PRZELEWY24 operator.
        :param str payment_id: The payment ID.
        :param str participant_login: Login of the participant. In case of REFUND_INCREASE operation this is the login of the seller, in other cases, of the buyer.
        :param datetime occurred_at_gte: The minimum date and time of operation occurrence in ISO 8601 format.
        :param datetime occurred_at_lte: The maximum date and time of operation occurrence in ISO 8601 format.
        :param list[str] group: Group of operation types: * INCOME - CONTRIBUTION, SURCHARGE, CORRECTION, DEDUCTION_INCREASE. * OUTCOME - PAYOUT, PAYOUT_CANCEL, DEDUCTION_CHARGE. * REFUND - REFUND_CHARGE, REFUND_CANCEL, REFUND_INCREASE, CORRECTION.
        :param int limit: Number of returned operations.
        :param int offset: Index of the first returned payment operation from all search results.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PaymentOperations
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_payments_operation_history_with_http_info(**kwargs)  # noqa: E501

    def get_payments_operation_history_with_http_info(self, **kwargs):  # noqa: E501
        """Payment operations history  # noqa: E501

        Use this endpoint to get the list of the seller's payment operations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payments_operation_history_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str wallet_type: Type of the wallet: * AVAILABLE - operations available for payout. * WAITING - operations temporarily suspended for payout.
        :param str wallet_payment_operator: Payment operator: * PAYU - operations processed by PAYU operator. * P24 - operations processed by PRZELEWY24 operator.
        :param str payment_id: The payment ID.
        :param str participant_login: Login of the participant. In case of REFUND_INCREASE operation this is the login of the seller, in other cases, of the buyer.
        :param datetime occurred_at_gte: The minimum date and time of operation occurrence in ISO 8601 format.
        :param datetime occurred_at_lte: The maximum date and time of operation occurrence in ISO 8601 format.
        :param list[str] group: Group of operation types: * INCOME - CONTRIBUTION, SURCHARGE, CORRECTION, DEDUCTION_INCREASE. * OUTCOME - PAYOUT, PAYOUT_CANCEL, DEDUCTION_CHARGE. * REFUND - REFUND_CHARGE, REFUND_CANCEL, REFUND_INCREASE, CORRECTION.
        :param int limit: Number of returned operations.
        :param int offset: Index of the first returned payment operation from all search results.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PaymentOperations, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['wallet_type', 'wallet_payment_operator', 'payment_id', 'participant_login', 'occurred_at_gte', 'occurred_at_lte', 'group', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payments_operation_history" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 50:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_payments_operation_history`, must be a value less than or equal to `50`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_payments_operation_history`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] > 10000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `get_payments_operation_history`, must be a value less than or equal to `10000`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `get_payments_operation_history`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'wallet_type' in local_var_params and local_var_params['wallet_type'] is not None:  # noqa: E501
            query_params.append(('wallet.type', local_var_params['wallet_type']))  # noqa: E501
        if 'wallet_payment_operator' in local_var_params and local_var_params['wallet_payment_operator'] is not None:  # noqa: E501
            query_params.append(('wallet.paymentOperator', local_var_params['wallet_payment_operator']))  # noqa: E501
        if 'payment_id' in local_var_params and local_var_params['payment_id'] is not None:  # noqa: E501
            query_params.append(('payment.id', local_var_params['payment_id']))  # noqa: E501
        if 'participant_login' in local_var_params and local_var_params['participant_login'] is not None:  # noqa: E501
            query_params.append(('participant.login', local_var_params['participant_login']))  # noqa: E501
        if 'occurred_at_gte' in local_var_params and local_var_params['occurred_at_gte'] is not None:  # noqa: E501
            query_params.append(('occurredAt.gte', local_var_params['occurred_at_gte']))  # noqa: E501
        if 'occurred_at_lte' in local_var_params and local_var_params['occurred_at_lte'] is not None:  # noqa: E501
            query_params.append(('occurredAt.lte', local_var_params['occurred_at_lte']))  # noqa: E501
        if 'group' in local_var_params and local_var_params['group'] is not None:  # noqa: E501
            query_params.append(('group', local_var_params['group']))  # noqa: E501
            collection_formats['group'] = 'multi'  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

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
            '/payments/payment-operations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaymentOperations',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_refunded_payments(self, **kwargs):  # noqa: E501
        """Get a list of refunded payments  # noqa: E501

        Get a list of refunded payments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_refunded_payments(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: Number of returned operations.
        :param int offset: Index of the first returned payment operation from all search results.
        :param str id: ID of the refund.
        :param str payment_id: ID of the payment.
        :param datetime occurred_at_gte: Minimum date and time when the refund occurred provided in ISO 8601 format.
        :param datetime occurred_at_lte: Maximum date and time when the refund occurred provided in ISO 8601 format.
        :param list[str] status: Current status of payment refund.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_refunded_payments_with_http_info(**kwargs)  # noqa: E501

    def get_refunded_payments_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of refunded payments  # noqa: E501

        Get a list of refunded payments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_refunded_payments_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: Number of returned operations.
        :param int offset: Index of the first returned payment operation from all search results.
        :param str id: ID of the refund.
        :param str payment_id: ID of the payment.
        :param datetime occurred_at_gte: Minimum date and time when the refund occurred provided in ISO 8601 format.
        :param datetime occurred_at_lte: Maximum date and time when the refund occurred provided in ISO 8601 format.
        :param list[str] status: Current status of payment refund.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(object, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['limit', 'offset', 'id', 'payment_id', 'occurred_at_gte', 'occurred_at_lte', 'status']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_refunded_payments" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_refunded_payments`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_refunded_payments`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `get_refunded_payments`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'id' in local_var_params and local_var_params['id'] is not None:  # noqa: E501
            query_params.append(('id', local_var_params['id']))  # noqa: E501
        if 'payment_id' in local_var_params and local_var_params['payment_id'] is not None:  # noqa: E501
            query_params.append(('payment.id', local_var_params['payment_id']))  # noqa: E501
        if 'occurred_at_gte' in local_var_params and local_var_params['occurred_at_gte'] is not None:  # noqa: E501
            query_params.append(('occurredAt.gte', local_var_params['occurred_at_gte']))  # noqa: E501
        if 'occurred_at_lte' in local_var_params and local_var_params['occurred_at_lte'] is not None:  # noqa: E501
            query_params.append(('occurredAt.lte', local_var_params['occurred_at_lte']))  # noqa: E501
        if 'status' in local_var_params and local_var_params['status'] is not None:  # noqa: E501
            query_params.append(('status', local_var_params['status']))  # noqa: E501
            collection_formats['status'] = 'multi'  # noqa: E501

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
            '/payments/refunds', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def initiate_refund(self, **kwargs):  # noqa: E501
        """Initiate a refund of a payment  # noqa: E501

        Use this endpoint to initiate a refund of a payment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.initiate_refund(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param InitializeRefund initialize_refund:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: RefundDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.initiate_refund_with_http_info(**kwargs)  # noqa: E501

    def initiate_refund_with_http_info(self, **kwargs):  # noqa: E501
        """Initiate a refund of a payment  # noqa: E501

        Use this endpoint to initiate a refund of a payment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.initiate_refund_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param InitializeRefund initialize_refund:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(RefundDetails, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['initialize_refund']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method initiate_refund" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'initialize_refund' in local_var_params:
            body_params = local_var_params['initialize_refund']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.allegro.public.v1+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/vnd.allegro.public.v1+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer-token-for-user']  # noqa: E501

        return self.api_client.call_api(
            '/payments/refunds', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RefundDetails',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
