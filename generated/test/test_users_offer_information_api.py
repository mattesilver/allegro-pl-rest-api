# coding: utf-8

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    The version of the OpenAPI document: 2020.03.12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import allegro_api
from allegro_api.api.users_offer_information_api import UsersOfferInformationApi  # noqa: E501
from allegro_api.rest import ApiException


class TestUsersOfferInformationApi(unittest.TestCase):
    """UsersOfferInformationApi unit test stubs"""

    def setUp(self):
        self.api = allegro_api.api.users_offer_information_api.UsersOfferInformationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_offer_events(self):
        """Test case for get_offer_events

        Get events about the seller's offers  # noqa: E501
        """
        pass

    def test_get_offer_using_get(self):
        """Test case for get_offer_using_get

        Get all fields of the particular offer  # noqa: E501
        """
        pass

    def test_search_offers_using_get(self):
        """Test case for search_offers_using_get

        Get seller's offers  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
