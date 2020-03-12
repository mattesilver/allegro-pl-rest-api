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


class OfferImageUploadResponse(object):
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
        'expires_at': 'datetime',
        'location': 'str'
    }

    attribute_map = {
        'expires_at': 'expiresAt',
        'location': 'location'
    }

    def __init__(self, expires_at=None, location=None, local_vars_configuration=None):  # noqa: E501
        """OfferImageUploadResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._expires_at = None
        self._location = None
        self.discriminator = None

        if expires_at is not None:
            self.expires_at = expires_at
        if location is not None:
            self.location = location

    @property
    def expires_at(self):
        """Gets the expires_at of this OfferImageUploadResponse.  # noqa: E501

        Date of file expiration (removal from the server). We will remove it unless you use it in your offer.  # noqa: E501

        :return: The expires_at of this OfferImageUploadResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this OfferImageUploadResponse.

        Date of file expiration (removal from the server). We will remove it unless you use it in your offer.  # noqa: E501

        :param expires_at: The expires_at of this OfferImageUploadResponse.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def location(self):
        """Gets the location of this OfferImageUploadResponse.  # noqa: E501

        Link to the uploaded image  # noqa: E501

        :return: The location of this OfferImageUploadResponse.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this OfferImageUploadResponse.

        Link to the uploaded image  # noqa: E501

        :param location: The location of this OfferImageUploadResponse.  # noqa: E501
        :type: str
        """

        self._location = location

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
        if not isinstance(other, OfferImageUploadResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OfferImageUploadResponse):
            return True

        return self.to_dict() != other.to_dict()