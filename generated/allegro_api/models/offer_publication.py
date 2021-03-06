# coding: utf-8

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    The version of the OpenAPI document: 2020.03.12
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from allegro_api.configuration import Configuration


class OfferPublication(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'ending_at': 'str'
    }

    attribute_map = {
        'ending_at': 'endingAt'
    }

    def __init__(self, ending_at=None, local_vars_configuration=None):  # noqa: E501
        """OfferPublication - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ending_at = None
        self.discriminator = None

        if ending_at is not None:
            self.ending_at = ending_at

    @property
    def ending_at(self):
        """Gets the ending_at of this OfferPublication.  # noqa: E501

        Publication ending date and time in UTC.  # noqa: E501

        :return: The ending_at of this OfferPublication.  # noqa: E501
        :rtype: str
        """
        return self._ending_at

    @ending_at.setter
    def ending_at(self, ending_at):
        """Sets the ending_at of this OfferPublication.

        Publication ending date and time in UTC.  # noqa: E501

        :param ending_at: The ending_at of this OfferPublication.  # noqa: E501
        :type: str
        """

        self._ending_at = ending_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OfferPublication):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OfferPublication):
            return True

        return self.to_dict() != other.to_dict()
