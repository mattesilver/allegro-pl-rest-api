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
from allegro_api.models.line_item_id_mappings import LineItemIdMappings  # noqa: E501
from allegro_api.rest import ApiException

class TestLineItemIdMappings(unittest.TestCase):
    """LineItemIdMappings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LineItemIdMappings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.line_item_id_mappings.LineItemIdMappings()  # noqa: E501
        if include_optional :
            return LineItemIdMappings(
                mappings = [
                    allegro_api.models.line_item_id_mappings_mappings.LineItemIdMappings_mappings(
                        deal_id = '12345678', 
                        line_item_id = '4e9d1d43-0da5-466e-9c4a-679625b7a617', )
                    ]
            )
        else :
            return LineItemIdMappings(
        )

    def testLineItemIdMappings(self):
        """Test LineItemIdMappings"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
