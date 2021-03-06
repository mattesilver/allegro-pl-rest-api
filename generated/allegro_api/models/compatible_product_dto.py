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


class CompatibleProductDto(object):
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
        'text': 'str',
        'group': 'CompatibleProductDtoGroup',
        'attributes': 'list[CompatibleProductDtoAttributes]'
    }

    attribute_map = {
        'id': 'id',
        'text': 'text',
        'group': 'group',
        'attributes': 'attributes'
    }

    def __init__(self, id=None, text=None, group=None, attributes=None, local_vars_configuration=None):  # noqa: E501
        """CompatibleProductDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._text = None
        self._group = None
        self._attributes = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if text is not None:
            self.text = text
        if group is not None:
            self.group = group
        if attributes is not None:
            self.attributes = attributes

    @property
    def id(self):
        """Gets the id of this CompatibleProductDto.  # noqa: E501

        Identifier of the compatible product.  # noqa: E501

        :return: The id of this CompatibleProductDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CompatibleProductDto.

        Identifier of the compatible product.  # noqa: E501

        :param id: The id of this CompatibleProductDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def text(self):
        """Gets the text of this CompatibleProductDto.  # noqa: E501

        Textual representation of the compatible product.  # noqa: E501

        :return: The text of this CompatibleProductDto.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this CompatibleProductDto.

        Textual representation of the compatible product.  # noqa: E501

        :param text: The text of this CompatibleProductDto.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def group(self):
        """Gets the group of this CompatibleProductDto.  # noqa: E501


        :return: The group of this CompatibleProductDto.  # noqa: E501
        :rtype: CompatibleProductDtoGroup
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this CompatibleProductDto.


        :param group: The group of this CompatibleProductDto.  # noqa: E501
        :type: CompatibleProductDtoGroup
        """

        self._group = group

    @property
    def attributes(self):
        """Gets the attributes of this CompatibleProductDto.  # noqa: E501

        List of compatible products attributes.  # noqa: E501

        :return: The attributes of this CompatibleProductDto.  # noqa: E501
        :rtype: list[CompatibleProductDtoAttributes]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this CompatibleProductDto.

        List of compatible products attributes.  # noqa: E501

        :param attributes: The attributes of this CompatibleProductDto.  # noqa: E501
        :type: list[CompatibleProductDtoAttributes]
        """

        self._attributes = attributes

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
        if not isinstance(other, CompatibleProductDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CompatibleProductDto):
            return True

        return self.to_dict() != other.to_dict()
