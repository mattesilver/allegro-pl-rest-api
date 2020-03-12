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
from allegro_api.api.billing_api import BillingApi  # noqa: E501
from allegro_api.rest import ApiException


class TestBillingApi(unittest.TestCase):
    """BillingApi unit test stubs"""

    def setUp(self):
        self.api = allegro_api.api.billing_api.BillingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_billing_entries(self):
        """Test case for get_billing_entries

        Get a list of billing entries  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()