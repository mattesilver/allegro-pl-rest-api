# coding: utf-8

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    OpenAPI spec version: latest
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from allegro_api.api_client import ApiClient


class ListingBadgesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_promotion_to_campaign_using_post(self, promotion_campaign_request_dto, **kwargs):  # noqa: E501
        """Create an application for a promotion campaign  # noqa: E501

        For an additional fee, you can place a discount mark on a list of offers.         You have to define promotion id and campaign section giving LISTING_BADGE as the id.         Your promotion campaign application will be verified and you will be notified of the verification status via e-mail.         Fees will be charged in accordance with Annex No. 1 to the Daily deals zone regulations.         More information about this resource you can find <a href=\"../../offer_bundles/#11\" target=\"_blank\">here</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_promotion_to_campaign_using_post(promotion_campaign_request_dto, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PromotionCampaignRequestDto promotion_campaign_request_dto: request (required)
        :return: PromotionCampaignResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_promotion_to_campaign_using_post_with_http_info(promotion_campaign_request_dto, **kwargs)  # noqa: E501
        else:
            (data) = self.add_promotion_to_campaign_using_post_with_http_info(promotion_campaign_request_dto, **kwargs)  # noqa: E501
            return data

    def add_promotion_to_campaign_using_post_with_http_info(self, promotion_campaign_request_dto, **kwargs):  # noqa: E501
        """Create an application for a promotion campaign  # noqa: E501

        For an additional fee, you can place a discount mark on a list of offers.         You have to define promotion id and campaign section giving LISTING_BADGE as the id.         Your promotion campaign application will be verified and you will be notified of the verification status via e-mail.         Fees will be charged in accordance with Annex No. 1 to the Daily deals zone regulations.         More information about this resource you can find <a href=\"../../offer_bundles/#11\" target=\"_blank\">here</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_promotion_to_campaign_using_post_with_http_info(promotion_campaign_request_dto, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PromotionCampaignRequestDto promotion_campaign_request_dto: request (required)
        :return: PromotionCampaignResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['promotion_campaign_request_dto']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_promotion_to_campaign_using_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'promotion_campaign_request_dto' is set
        if ('promotion_campaign_request_dto' not in local_var_params or
                local_var_params['promotion_campaign_request_dto'] is None):
            raise ValueError("Missing the required parameter `promotion_campaign_request_dto` when calling `add_promotion_to_campaign_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'promotion_campaign_request_dto' in local_var_params:
            body_params = local_var_params['promotion_campaign_request_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.allegro.public.v1+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/vnd.allegro.public.v1+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer-token-for-user']  # noqa: E501

        return self.api_client.call_api(
            '/sale/loyalty/promotion-campaigns', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PromotionCampaignResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_campaign_from_promotion_using_delete(self, promotion_id, campaign_id, **kwargs):  # noqa: E501
        """Delete a campaign in a promotion  # noqa: E501

        Use this resource to delete campaign from promotion by promotion id and campaign id. More information about this resource you can find <a href=\"../../offer_bundles/#16\" target=\"_blank\">here</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_campaign_from_promotion_using_delete(promotion_id, campaign_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str promotion_id: The promotion unique id (required)
        :param str campaign_id: The campaign unique id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_campaign_from_promotion_using_delete_with_http_info(promotion_id, campaign_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_campaign_from_promotion_using_delete_with_http_info(promotion_id, campaign_id, **kwargs)  # noqa: E501
            return data

    def delete_campaign_from_promotion_using_delete_with_http_info(self, promotion_id, campaign_id, **kwargs):  # noqa: E501
        """Delete a campaign in a promotion  # noqa: E501

        Use this resource to delete campaign from promotion by promotion id and campaign id. More information about this resource you can find <a href=\"../../offer_bundles/#16\" target=\"_blank\">here</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_campaign_from_promotion_using_delete_with_http_info(promotion_id, campaign_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str promotion_id: The promotion unique id (required)
        :param str campaign_id: The campaign unique id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['promotion_id', 'campaign_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_campaign_from_promotion_using_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'promotion_id' is set
        if ('promotion_id' not in local_var_params or
                local_var_params['promotion_id'] is None):
            raise ValueError("Missing the required parameter `promotion_id` when calling `delete_campaign_from_promotion_using_delete`")  # noqa: E501
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in local_var_params or
                local_var_params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `delete_campaign_from_promotion_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'promotion_id' in local_var_params:
            query_params.append(('promotion.id', local_var_params['promotion_id']))  # noqa: E501
        if 'campaign_id' in local_var_params:
            query_params.append(('campaign.id', local_var_params['campaign_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer-token-for-user']  # noqa: E501

        return self.api_client.call_api(
            '/sale/loyalty/promotion-campaigns', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_promotion_campaign_application_using_delete(self, application_id, **kwargs):  # noqa: E501
        """Delete an application for promotion campaign  # noqa: E501

        Use this resource to delete promotion campaign application by application id. You need to use its unique id. More information about this resource you can find <a href=\"../../offer_bundles/#15\" target=\"_blank\">here</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_promotion_campaign_application_using_delete(application_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: The application unique id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_promotion_campaign_application_using_delete_with_http_info(application_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_promotion_campaign_application_using_delete_with_http_info(application_id, **kwargs)  # noqa: E501
            return data

    def delete_promotion_campaign_application_using_delete_with_http_info(self, application_id, **kwargs):  # noqa: E501
        """Delete an application for promotion campaign  # noqa: E501

        Use this resource to delete promotion campaign application by application id. You need to use its unique id. More information about this resource you can find <a href=\"../../offer_bundles/#15\" target=\"_blank\">here</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_promotion_campaign_application_using_delete_with_http_info(application_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: The application unique id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['application_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_promotion_campaign_application_using_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'application_id' is set
        if ('application_id' not in local_var_params or
                local_var_params['application_id'] is None):
            raise ValueError("Missing the required parameter `application_id` when calling `delete_promotion_campaign_application_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['applicationId'] = local_var_params['application_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer-token-for-user']  # noqa: E501

        return self.api_client.call_api(
            '/sale/loyalty/promotion-campaign-applications/{applicationId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_promotion_campaign_application_using_get(self, application_id, **kwargs):  # noqa: E501
        """Get an application for promotion campaign  # noqa: E501

        Use this resource to retrieve promotion campaign application. You need to use its unique id. More information about this resource you can find <a href=\"../../offer_bundles/#12\" target=\"_blank\">here</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_promotion_campaign_application_using_get(application_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: The application unique id (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_promotion_campaign_application_using_get_with_http_info(application_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_promotion_campaign_application_using_get_with_http_info(application_id, **kwargs)  # noqa: E501
            return data

    def get_promotion_campaign_application_using_get_with_http_info(self, application_id, **kwargs):  # noqa: E501
        """Get an application for promotion campaign  # noqa: E501

        Use this resource to retrieve promotion campaign application. You need to use its unique id. More information about this resource you can find <a href=\"../../offer_bundles/#12\" target=\"_blank\">here</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_promotion_campaign_application_using_get_with_http_info(application_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: The application unique id (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['application_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_promotion_campaign_application_using_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'application_id' is set
        if ('application_id' not in local_var_params or
                local_var_params['application_id'] is None):
            raise ValueError("Missing the required parameter `application_id` when calling `get_promotion_campaign_application_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['applicationId'] = local_var_params['application_id']  # noqa: E501

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
            '/sale/loyalty/promotion-campaign-applications/{applicationId}', 'GET',
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

    def get_promotion_campaigns_using_get(self, **kwargs):  # noqa: E501
        """Get the user's promotion campaigns  # noqa: E501

        Use this resource to retrieve promotion campaigns. You can find promotion campaign by promotion id. More information about this resource you can find <a href=\"../../offer_bundles/#13\" target=\"_blank\">here</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_promotion_campaigns_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str promotion_id: The promotion unique id
        :param int limit: limit
        :param int offset: offset
        :return: PromotionCampaignsResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_promotion_campaigns_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_promotion_campaigns_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_promotion_campaigns_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get the user's promotion campaigns  # noqa: E501

        Use this resource to retrieve promotion campaigns. You can find promotion campaign by promotion id. More information about this resource you can find <a href=\"../../offer_bundles/#13\" target=\"_blank\">here</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_promotion_campaigns_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str promotion_id: The promotion unique id
        :param int limit: limit
        :param int offset: offset
        :return: PromotionCampaignsResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['promotion_id', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_promotion_campaigns_using_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'promotion_id' in local_var_params:
            query_params.append(('promotion.id', local_var_params['promotion_id']))  # noqa: E501
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params:
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
            '/sale/loyalty/promotion-campaigns', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PromotionCampaignsResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)