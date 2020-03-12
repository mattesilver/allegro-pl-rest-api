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
from allegro_api.api.badge_campaigns_api import BadgeCampaignsApi  # noqa: E501
from allegro_api.rest import ApiException


class TestBadgeCampaignsApi(unittest.TestCase):
    """BadgeCampaignsApi unit test stubs"""

    def setUp(self):
        self.api = allegro_api.api.badge_campaigns_api.BadgeCampaignsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_badge_applications_get_all(self):
        """Test case for badge_applications_get_all

        [BETA] Get a list of badge applications  # noqa: E501
        """
        pass

    def test_badge_applications_get_one(self):
        """Test case for badge_applications_get_one

        [BETA] Get a badge application details  # noqa: E501
        """
        pass

    def test_badge_campaigns_get_all(self):
        """Test case for badge_campaigns_get_all

        [BETA] Get a list of available badge campaigns  # noqa: E501
        """
        pass

    def test_get_badges(self):
        """Test case for get_badges

        [BETA] Get a list of badges  # noqa: E501
        """
        pass

    def test_post_badges(self):
        """Test case for post_badges

        [BETA] Apply for badge in selected offer  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()