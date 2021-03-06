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
from allegro_api.models.base_operation import BaseOperation  # noqa: E501
from allegro_api.rest import ApiException

class TestBaseOperation(unittest.TestCase):
    """BaseOperation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BaseOperation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.base_operation.BaseOperation()  # noqa: E501
        if include_optional :
            return BaseOperation(
                type = '0', 
                group = 'INCOME', 
                wallet = allegro_api.models.wallet.Wallet(
                    payment_operator = 'PAYU', 
                    type = 'AVAILABLE', 
                    balance = null, ), 
                value = null, 
                occurred_at = '2019-05-08T09:45:00.818Z'
            )
        else :
            return BaseOperation(
                type = '0',
                group = 'INCOME',
                wallet = allegro_api.models.wallet.Wallet(
                    payment_operator = 'PAYU', 
                    type = 'AVAILABLE', 
                    balance = null, ),
                value = null,
                occurred_at = '2019-05-08T09:45:00.818Z',
        )

    def testBaseOperation(self):
        """Test BaseOperation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
