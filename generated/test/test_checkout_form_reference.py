# coding: utf-8

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    The version of the OpenAPI document: 2020.03.12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import allegro_api
from allegro_api.models.checkout_form_reference import CheckoutFormReference  # noqa: E501
from allegro_api.rest import ApiException

class TestCheckoutFormReference(unittest.TestCase):
    """CheckoutFormReference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CheckoutFormReference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.checkout_form_reference.CheckoutFormReference()  # noqa: E501
        if include_optional :
            return CheckoutFormReference(
                id = '88ae369b-8f65-4fc4-9c77-bedf604a2e2b'
            )
        else :
            return CheckoutFormReference(
                id = '88ae369b-8f65-4fc4-9c77-bedf604a2e2b',
        )

    def testCheckoutFormReference(self):
        """Test CheckoutFormReference"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
