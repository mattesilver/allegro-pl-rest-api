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
from allegro_api.models.inline_response2001_delivery_methods import InlineResponse2001DeliveryMethods  # noqa: E501
from allegro_api.rest import ApiException

class TestInlineResponse2001DeliveryMethods(unittest.TestCase):
    """InlineResponse2001DeliveryMethods unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2001DeliveryMethods
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.inline_response2001_delivery_methods.InlineResponse2001DeliveryMethods()  # noqa: E501
        if include_optional :
            return InlineResponse2001DeliveryMethods(
                id = '0', 
                name = '0', 
                payment_policy = 'IN_ADVANCE', 
                allegro_endorsed = True, 
                shipping_rates_constraints = allegro_api.models.inline_response_200_1_shipping_rates_constraints.inline_response_200_1_shippingRatesConstraints(
                    allowed = True, 
                    max_quantity_per_package = allegro_api.models.inline_response_200_1_shipping_rates_constraints_max_quantity_per_package.inline_response_200_1_shippingRatesConstraints_maxQuantityPerPackage(
                        max = 999999, ), 
                    first_item_rate = allegro_api.models.inline_response_200_1_shipping_rates_constraints_first_item_rate.inline_response_200_1_shippingRatesConstraints_firstItemRate(
                        min = '0.00', 
                        max = '8.99', 
                        currency = 'PLN', ), 
                    next_item_rate = allegro_api.models.inline_response_200_1_shipping_rates_constraints_next_item_rate.inline_response_200_1_shippingRatesConstraints_nextItemRate(
                        min = '0.00', 
                        max = '8.99', 
                        currency = 'PLN', ), 
                    shipping_time = allegro_api.models.inline_response_200_1_shipping_rates_constraints_shipping_time.inline_response_200_1_shippingRatesConstraints_shippingTime(
                        default = allegro_api.models.inline_response_200_1_shipping_rates_constraints_shipping_time_default.inline_response_200_1_shippingRatesConstraints_shippingTime_default(
                            from = 'PT24H', 
                            to = 'PT48H', ), 
                        customizable = True, ), )
            )
        else :
            return InlineResponse2001DeliveryMethods(
        )

    def testInlineResponse2001DeliveryMethods(self):
        """Test InlineResponse2001DeliveryMethods"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
