# coding: utf-8

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    OpenAPI spec version: latest
    Generated by: https://openapi-generator.tech
"""

import pprint

import six

from .category_parameter import CategoryParameter


class DictionaryCategoryParameter(CategoryParameter):
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
        'type': 'str',
        'restrictions': 'object',
        'dictionary': 'list[object]'
        , 'id': 'str',
        'name': 'str',
        'required': 'bool',
        'unit': 'str',
        'options': 'CategoryParameterOptions'
    }

    attribute_map = {
        'type': 'type',
        'restrictions': 'restrictions',
        'dictionary': 'dictionary'
        , 'id': 'id',
        'name': 'name',
        'required': 'required',
        'unit': 'unit',
        'options': 'options'
    }

    def __init__(self, id, name=None, required=None, unit=None, options=None, type='dictionary', restrictions=None,
                 dictionary=None):
        """DictionaryCategoryParameter - a model defined in OpenAPI"""  # noqa: E501

        super().__init__(id, name, type, required, unit, options)

        self._restrictions = None
        self._dictionary = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if restrictions is not None:
            self.restrictions = restrictions
        if dictionary is not None:
            self.dictionary = dictionary

    @property
    def type(self):
        """Gets the type of this DictionaryCategoryParameter.  # noqa: E501


        :return: The type of this DictionaryCategoryParameter.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DictionaryCategoryParameter.


        :param type: The type of this DictionaryCategoryParameter.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def restrictions(self):
        """Gets the restrictions of this DictionaryCategoryParameter.  # noqa: E501


        :return: The restrictions of this DictionaryCategoryParameter.  # noqa: E501
        :rtype: object
        """
        return self._restrictions

    @restrictions.setter
    def restrictions(self, restrictions):
        """Sets the restrictions of this DictionaryCategoryParameter.


        :param restrictions: The restrictions of this DictionaryCategoryParameter.  # noqa: E501
        :type: object
        """

        self._restrictions = restrictions

    @property
    def dictionary(self):
        """Gets the dictionary of this DictionaryCategoryParameter.  # noqa: E501


        :return: The dictionary of this DictionaryCategoryParameter.  # noqa: E501
        :rtype: list[object]
        """
        return self._dictionary

    @dictionary.setter
    def dictionary(self, dictionary):
        """Sets the dictionary of this DictionaryCategoryParameter.


        :param dictionary: The dictionary of this DictionaryCategoryParameter.  # noqa: E501
        :type: list[object]
        """

        self._dictionary = dictionary

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
        if not isinstance(other, DictionaryCategoryParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
