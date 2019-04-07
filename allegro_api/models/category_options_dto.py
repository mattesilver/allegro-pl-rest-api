# coding: utf-8

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    OpenAPI spec version: latest
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class CategoryOptionsDto(object):
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
        'advertisement': 'bool',
        'advertisement_price_optional': 'bool',
        'variants_by_color_pattern_allowed': 'bool',
        'offers_with_product_publication_enabled': 'bool'
    }

    attribute_map = {
        'advertisement': 'advertisement',
        'advertisement_price_optional': 'advertisementPriceOptional',
        'variants_by_color_pattern_allowed': 'variantsByColorPatternAllowed',
        'offers_with_product_publication_enabled': 'offersWithProductPublicationEnabled'
    }

    def __init__(self, advertisement=None, advertisement_price_optional=None, variants_by_color_pattern_allowed=None, offers_with_product_publication_enabled=None):  # noqa: E501
        """CategoryOptionsDto - a model defined in OpenAPI"""  # noqa: E501

        self._advertisement = None
        self._advertisement_price_optional = None
        self._variants_by_color_pattern_allowed = None
        self._offers_with_product_publication_enabled = None
        self.discriminator = None

        if advertisement is not None:
            self.advertisement = advertisement
        if advertisement_price_optional is not None:
            self.advertisement_price_optional = advertisement_price_optional
        if variants_by_color_pattern_allowed is not None:
            self.variants_by_color_pattern_allowed = variants_by_color_pattern_allowed
        if offers_with_product_publication_enabled is not None:
            self.offers_with_product_publication_enabled = offers_with_product_publication_enabled

    @property
    def advertisement(self):
        """Gets the advertisement of this CategoryOptionsDto.  # noqa: E501


        :return: The advertisement of this CategoryOptionsDto.  # noqa: E501
        :rtype: bool
        """
        return self._advertisement

    @advertisement.setter
    def advertisement(self, advertisement):
        """Sets the advertisement of this CategoryOptionsDto.


        :param advertisement: The advertisement of this CategoryOptionsDto.  # noqa: E501
        :type: bool
        """

        self._advertisement = advertisement

    @property
    def advertisement_price_optional(self):
        """Gets the advertisement_price_optional of this CategoryOptionsDto.  # noqa: E501


        :return: The advertisement_price_optional of this CategoryOptionsDto.  # noqa: E501
        :rtype: bool
        """
        return self._advertisement_price_optional

    @advertisement_price_optional.setter
    def advertisement_price_optional(self, advertisement_price_optional):
        """Sets the advertisement_price_optional of this CategoryOptionsDto.


        :param advertisement_price_optional: The advertisement_price_optional of this CategoryOptionsDto.  # noqa: E501
        :type: bool
        """

        self._advertisement_price_optional = advertisement_price_optional

    @property
    def variants_by_color_pattern_allowed(self):
        """Gets the variants_by_color_pattern_allowed of this CategoryOptionsDto.  # noqa: E501


        :return: The variants_by_color_pattern_allowed of this CategoryOptionsDto.  # noqa: E501
        :rtype: bool
        """
        return self._variants_by_color_pattern_allowed

    @variants_by_color_pattern_allowed.setter
    def variants_by_color_pattern_allowed(self, variants_by_color_pattern_allowed):
        """Sets the variants_by_color_pattern_allowed of this CategoryOptionsDto.


        :param variants_by_color_pattern_allowed: The variants_by_color_pattern_allowed of this CategoryOptionsDto.  # noqa: E501
        :type: bool
        """

        self._variants_by_color_pattern_allowed = variants_by_color_pattern_allowed

    @property
    def offers_with_product_publication_enabled(self):
        """Gets the offers_with_product_publication_enabled of this CategoryOptionsDto.  # noqa: E501


        :return: The offers_with_product_publication_enabled of this CategoryOptionsDto.  # noqa: E501
        :rtype: bool
        """
        return self._offers_with_product_publication_enabled

    @offers_with_product_publication_enabled.setter
    def offers_with_product_publication_enabled(self, offers_with_product_publication_enabled):
        """Sets the offers_with_product_publication_enabled of this CategoryOptionsDto.


        :param offers_with_product_publication_enabled: The offers_with_product_publication_enabled of this CategoryOptionsDto.  # noqa: E501
        :type: bool
        """

        self._offers_with_product_publication_enabled = offers_with_product_publication_enabled

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
        if not isinstance(other, CategoryOptionsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
