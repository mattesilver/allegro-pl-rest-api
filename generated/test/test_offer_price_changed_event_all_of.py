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
from allegro_api.models.offer_price_changed_event_all_of import OfferPriceChangedEventAllOf  # noqa: E501
from allegro_api.rest import ApiException

class TestOfferPriceChangedEventAllOf(unittest.TestCase):
    """OfferPriceChangedEventAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OfferPriceChangedEventAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.offer_price_changed_event_all_of.OfferPriceChangedEventAllOf()  # noqa: E501
        if include_optional :
            return OfferPriceChangedEventAllOf(
                type = 'OFFER_PRICE_CHANGED', 
                offer = allegro_api.models.offer_event_base_offer.OfferEventBaseOffer(
                    id = '2865624934', )
            )
        else :
            return OfferPriceChangedEventAllOf(
                offer = allegro_api.models.offer_event_base_offer.OfferEventBaseOffer(
                    id = '2865624934', ),
        )

    def testOfferPriceChangedEventAllOf(self):
        """Test OfferPriceChangedEventAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
