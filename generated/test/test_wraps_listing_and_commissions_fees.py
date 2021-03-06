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
from allegro_api.models.wraps_listing_and_commissions_fees import WrapsListingAndCommissionsFees  # noqa: E501
from allegro_api.rest import ApiException

class TestWrapsListingAndCommissionsFees(unittest.TestCase):
    """WrapsListingAndCommissionsFees unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WrapsListingAndCommissionsFees
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.wraps_listing_and_commissions_fees.WrapsListingAndCommissionsFees()  # noqa: E501
        if include_optional :
            return WrapsListingAndCommissionsFees(
                commissions = [
                    allegro_api.models.describes_success_commission_fee.Describes_success_commission_fee(
                        fee = allegro_api.models.fee.Fee(
                            amount = '0', 
                            currency = '0', ), 
                        name = '0', 
                        type = '0', )
                    ], 
                quotes = [
                    allegro_api.models.describes_listing_fee.Describes_listing_fee(
                        fee = allegro_api.models.fee.Fee(
                            amount = '0', 
                            currency = '0', ), 
                        name = '0', 
                        type = '0', 
                        cycle_duration = 'PT240H', )
                    ]
            )
        else :
            return WrapsListingAndCommissionsFees(
                commissions = [
                    allegro_api.models.describes_success_commission_fee.Describes_success_commission_fee(
                        fee = allegro_api.models.fee.Fee(
                            amount = '0', 
                            currency = '0', ), 
                        name = '0', 
                        type = '0', )
                    ],
                quotes = [
                    allegro_api.models.describes_listing_fee.Describes_listing_fee(
                        fee = allegro_api.models.fee.Fee(
                            amount = '0', 
                            currency = '0', ), 
                        name = '0', 
                        type = '0', 
                        cycle_duration = 'PT240H', )
                    ],
        )

    def testWrapsListingAndCommissionsFees(self):
        """Test WrapsListingAndCommissionsFees"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
