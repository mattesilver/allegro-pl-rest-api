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
from allegro_api.api.compatibility_list_api import CompatibilityListApi  # noqa: E501
from allegro_api.rest import ApiException


class TestCompatibilityListApi(unittest.TestCase):
    """CompatibilityListApi unit test stubs"""

    def setUp(self):
        self.api = allegro_api.api.compatibility_list_api.CompatibilityListApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_categories_that_support_compatibility_list(self):
        """Test case for get_categories_that_support_compatibility_list

        Get list of categories where compatibility list is supported  # noqa: E501
        """
        pass

    def test_get_compatible_products(self):
        """Test case for get_compatible_products

        Get list of compatible products  # noqa: E501
        """
        pass

    def test_get_compatible_products_groups(self):
        """Test case for get_compatible_products_groups

        Get list of compatible product groups  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
