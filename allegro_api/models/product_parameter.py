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


class ProductParameter(object):
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
        'id': 'str',
        'range_value': 'ParameterRangeValue',
        'values': 'list[str]',
        'values_ids': 'list[str]',
        'value_labels': 'list[str]',
        'options': 'list[ProductParameterOptions]'
    }

    attribute_map = {
        'id': 'id',
        'range_value': 'rangeValue',
        'values': 'values',
        'values_ids': 'valuesIds',
        'value_labels': 'valueLabels',
        'options': 'options'
    }

    def __init__(self, id=None, range_value=None, values=None, values_ids=None, value_labels=None, options=None):  # noqa: E501
        """ProductParameter - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._range_value = None
        self._values = None
        self._values_ids = None
        self._value_labels = None
        self._options = None
        self.discriminator = None

        self.id = id
        if range_value is not None:
            self.range_value = range_value
        if values is not None:
            self.values = values
        if values_ids is not None:
            self.values_ids = values_ids
        if value_labels is not None:
            self.value_labels = value_labels
        if options is not None:
            self.options = options

    @property
    def id(self):
        """Gets the id of this ProductParameter.  # noqa: E501


        :return: The id of this ProductParameter.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProductParameter.


        :param id: The id of this ProductParameter.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def range_value(self):
        """Gets the range_value of this ProductParameter.  # noqa: E501


        :return: The range_value of this ProductParameter.  # noqa: E501
        :rtype: ParameterRangeValue
        """
        return self._range_value

    @range_value.setter
    def range_value(self, range_value):
        """Sets the range_value of this ProductParameter.


        :param range_value: The range_value of this ProductParameter.  # noqa: E501
        :type: ParameterRangeValue
        """

        self._range_value = range_value

    @property
    def values(self):
        """Gets the values of this ProductParameter.  # noqa: E501


        :return: The values of this ProductParameter.  # noqa: E501
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ProductParameter.


        :param values: The values of this ProductParameter.  # noqa: E501
        :type: list[str]
        """

        self._values = values

    @property
    def values_ids(self):
        """Gets the values_ids of this ProductParameter.  # noqa: E501


        :return: The values_ids of this ProductParameter.  # noqa: E501
        :rtype: list[str]
        """
        return self._values_ids

    @values_ids.setter
    def values_ids(self, values_ids):
        """Sets the values_ids of this ProductParameter.


        :param values_ids: The values_ids of this ProductParameter.  # noqa: E501
        :type: list[str]
        """

        self._values_ids = values_ids

    @property
    def value_labels(self):
        """Gets the value_labels of this ProductParameter.  # noqa: E501


        :return: The value_labels of this ProductParameter.  # noqa: E501
        :rtype: list[str]
        """
        return self._value_labels

    @value_labels.setter
    def value_labels(self, value_labels):
        """Sets the value_labels of this ProductParameter.


        :param value_labels: The value_labels of this ProductParameter.  # noqa: E501
        :type: list[str]
        """

        self._value_labels = value_labels

    @property
    def options(self):
        """Gets the options of this ProductParameter.  # noqa: E501


        :return: The options of this ProductParameter.  # noqa: E501
        :rtype: list[ProductParameterOptions]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this ProductParameter.


        :param options: The options of this ProductParameter.  # noqa: E501
        :type: list[ProductParameterOptions]
        """

        self._options = options

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
        if not isinstance(other, ProductParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
