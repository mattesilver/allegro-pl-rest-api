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


class AfterSalesServices(object):
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
        'implied_warranty': 'JustId',
        'return_policy': 'JustId',
        'warranty': 'JustId'
    }

    attribute_map = {
        'implied_warranty': 'impliedWarranty',
        'return_policy': 'returnPolicy',
        'warranty': 'warranty'
    }

    def __init__(self, implied_warranty=None, return_policy=None, warranty=None):  # noqa: E501
        """AfterSalesServices - a model defined in OpenAPI"""  # noqa: E501

        self._implied_warranty = None
        self._return_policy = None
        self._warranty = None
        self.discriminator = None

        if implied_warranty is not None:
            self.implied_warranty = implied_warranty
        if return_policy is not None:
            self.return_policy = return_policy
        if warranty is not None:
            self.warranty = warranty

    @property
    def implied_warranty(self):
        """Gets the implied_warranty of this AfterSalesServices.  # noqa: E501


        :return: The implied_warranty of this AfterSalesServices.  # noqa: E501
        :rtype: JustId
        """
        return self._implied_warranty

    @implied_warranty.setter
    def implied_warranty(self, implied_warranty):
        """Sets the implied_warranty of this AfterSalesServices.


        :param implied_warranty: The implied_warranty of this AfterSalesServices.  # noqa: E501
        :type: JustId
        """

        self._implied_warranty = implied_warranty

    @property
    def return_policy(self):
        """Gets the return_policy of this AfterSalesServices.  # noqa: E501


        :return: The return_policy of this AfterSalesServices.  # noqa: E501
        :rtype: JustId
        """
        return self._return_policy

    @return_policy.setter
    def return_policy(self, return_policy):
        """Sets the return_policy of this AfterSalesServices.


        :param return_policy: The return_policy of this AfterSalesServices.  # noqa: E501
        :type: JustId
        """

        self._return_policy = return_policy

    @property
    def warranty(self):
        """Gets the warranty of this AfterSalesServices.  # noqa: E501


        :return: The warranty of this AfterSalesServices.  # noqa: E501
        :rtype: JustId
        """
        return self._warranty

    @warranty.setter
    def warranty(self, warranty):
        """Sets the warranty of this AfterSalesServices.


        :param warranty: The warranty of this AfterSalesServices.  # noqa: E501
        :type: JustId
        """

        self._warranty = warranty

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
        if not isinstance(other, AfterSalesServices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other