# coding: utf-8

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    OpenAPI spec version: latest
    Generated by: https://openapi-generator.tech
"""

import pprint

import six


class CategoryParameter(object):
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
    }

    attribute_map = {
    }

    discriminator_value_class_map = {
        'dictionary': 'DictionaryCategoryParameter',
        'float': 'FloatCategoryParameter',
        'integer': 'IntegerCategoryParameter',
        'string': 'StringCategoryParameter'
    }

    discriminator = 'type'

    def __init__(self, id=None, name=None, type='dictionary', required=None, unit=None, options=None):  # noqa: E501
        """CategoryParameter - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._type = None
        self._required = None
        self._unit = None
        self._options = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        self.type = type
        if required is not None:
            self.required = required
        if unit is not None:
            self.unit = unit
        if options is not None:
            self.options = options

    @property
    def id(self):
        """Gets the id of this CategoryParameter.  # noqa: E501


        :return: The id of this CategoryParameter.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CategoryParameter.


        :param id: The id of this CategoryParameter.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CategoryParameter.  # noqa: E501


        :return: The name of this CategoryParameter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CategoryParameter.


        :param name: The name of this CategoryParameter.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this CategoryParameter.  # noqa: E501


        :return: The type of this CategoryParameter.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CategoryParameter.


        :param type: The type of this CategoryParameter.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def required(self):
        """Gets the required of this CategoryParameter.  # noqa: E501


        :return: The required of this CategoryParameter.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this CategoryParameter.


        :param required: The required of this CategoryParameter.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def unit(self):
        """Gets the unit of this CategoryParameter.  # noqa: E501


        :return: The unit of this CategoryParameter.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this CategoryParameter.


        :param unit: The unit of this CategoryParameter.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def options(self):
        """Gets the options of this CategoryParameter.  # noqa: E501


        :return: The options of this CategoryParameter.  # noqa: E501
        :rtype: CategoryParameterOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this CategoryParameter.


        :param options: The options of this CategoryParameter.  # noqa: E501
        :type: CategoryParameterOptions
        """

        self._options = options

    @classmethod
    def get_real_child_model(cls, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[cls.discriminator]
        return cls.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, CategoryParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
