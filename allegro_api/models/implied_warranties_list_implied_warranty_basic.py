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


class ImpliedWarrantiesListImpliedWarrantyBasic(object):
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
        'count': 'int',
        'implied_warranties': 'list[ImpliedWarrantyBasic]'
    }

    attribute_map = {
        'count': 'count',
        'implied_warranties': 'impliedWarranties'
    }

    def __init__(self, count=None, implied_warranties=None):  # noqa: E501
        """ImpliedWarrantiesListImpliedWarrantyBasic - a model defined in OpenAPI"""  # noqa: E501

        self._count = None
        self._implied_warranties = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if implied_warranties is not None:
            self.implied_warranties = implied_warranties

    @property
    def count(self):
        """Gets the count of this ImpliedWarrantiesListImpliedWarrantyBasic.  # noqa: E501


        :return: The count of this ImpliedWarrantiesListImpliedWarrantyBasic.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ImpliedWarrantiesListImpliedWarrantyBasic.


        :param count: The count of this ImpliedWarrantiesListImpliedWarrantyBasic.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def implied_warranties(self):
        """Gets the implied_warranties of this ImpliedWarrantiesListImpliedWarrantyBasic.  # noqa: E501


        :return: The implied_warranties of this ImpliedWarrantiesListImpliedWarrantyBasic.  # noqa: E501
        :rtype: list[ImpliedWarrantyBasic]
        """
        return self._implied_warranties

    @implied_warranties.setter
    def implied_warranties(self, implied_warranties):
        """Sets the implied_warranties of this ImpliedWarrantiesListImpliedWarrantyBasic.


        :param implied_warranties: The implied_warranties of this ImpliedWarrantiesListImpliedWarrantyBasic.  # noqa: E501
        :type: list[ImpliedWarrantyBasic]
        """

        self._implied_warranties = implied_warranties

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
        if not isinstance(other, ImpliedWarrantiesListImpliedWarrantyBasic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other