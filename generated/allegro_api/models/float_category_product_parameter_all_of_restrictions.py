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


class FloatCategoryProductParameterAllOfRestrictions(object):
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
        'min': 'float',
        'max': 'float',
        'range': 'bool',
        'precision': 'int'
    }

    attribute_map = {
        'min': 'min',
        'max': 'max',
        'range': 'range',
        'precision': 'precision'
    }

    def __init__(self, min=None, max=None, range=None, precision=None, local_vars_configuration=None):  # noqa: E501
        """FloatCategoryProductParameterAllOfRestrictions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._min = None
        self._max = None
        self._range = None
        self._precision = None
        self.discriminator = None

        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if range is not None:
            self.range = range
        if precision is not None:
            self.precision = precision

    @property
    def min(self):
        """Gets the min of this FloatCategoryProductParameterAllOfRestrictions.  # noqa: E501

        The minimum value of this parameter.  # noqa: E501

        :return: The min of this FloatCategoryProductParameterAllOfRestrictions.  # noqa: E501
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this FloatCategoryProductParameterAllOfRestrictions.

        The minimum value of this parameter.  # noqa: E501

        :param min: The min of this FloatCategoryProductParameterAllOfRestrictions.  # noqa: E501
        :type: float
        """

        self._min = min

    @property
    def max(self):
        """Gets the max of this FloatCategoryProductParameterAllOfRestrictions.  # noqa: E501

        The maximum value of this parameter.  # noqa: E501

        :return: The max of this FloatCategoryProductParameterAllOfRestrictions.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this FloatCategoryProductParameterAllOfRestrictions.

        The maximum value of this parameter.  # noqa: E501

        :param max: The max of this FloatCategoryProductParameterAllOfRestrictions.  # noqa: E501
        :type: float
        """

        self._max = max

    @property
    def range(self):
        """Gets the range of this FloatCategoryProductParameterAllOfRestrictions.  # noqa: E501

        Indicates whether this is a range parameter. If this is `true`, then you have to provide two values for this parameter - `from` and `to`. Both these values have to be between the `min` and `max`.  # noqa: E501

        :return: The range of this FloatCategoryProductParameterAllOfRestrictions.  # noqa: E501
        :rtype: bool
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this FloatCategoryProductParameterAllOfRestrictions.

        Indicates whether this is a range parameter. If this is `true`, then you have to provide two values for this parameter - `from` and `to`. Both these values have to be between the `min` and `max`.  # noqa: E501

        :param range: The range of this FloatCategoryProductParameterAllOfRestrictions.  # noqa: E501
        :type: bool
        """

        self._range = range

    @property
    def precision(self):
        """Gets the precision of this FloatCategoryProductParameterAllOfRestrictions.  # noqa: E501

        Number of digits you can provide after a comma that can be transferred in the parameter value.  # noqa: E501

        :return: The precision of this FloatCategoryProductParameterAllOfRestrictions.  # noqa: E501
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """Sets the precision of this FloatCategoryProductParameterAllOfRestrictions.

        Number of digits you can provide after a comma that can be transferred in the parameter value.  # noqa: E501

        :param precision: The precision of this FloatCategoryProductParameterAllOfRestrictions.  # noqa: E501
        :type: int
        """

        self._precision = precision

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
        if not isinstance(other, FloatCategoryProductParameterAllOfRestrictions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FloatCategoryProductParameterAllOfRestrictions):
            return True

        return self.to_dict() != other.to_dict()
