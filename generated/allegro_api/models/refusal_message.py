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


class RefusalMessage(object):
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
        'text': 'str',
        'link': 'str'
    }

    attribute_map = {
        'text': 'text',
        'link': 'link'
    }

    def __init__(self, text=None, link=None, local_vars_configuration=None):  # noqa: E501
        """RefusalMessage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._text = None
        self._link = None
        self.discriminator = None

        self.text = text
        if link is not None:
            self.link = link

    @property
    def text(self):
        """Gets the text of this RefusalMessage.  # noqa: E501

        Detailed message.  # noqa: E501

        :return: The text of this RefusalMessage.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this RefusalMessage.

        Detailed message.  # noqa: E501

        :param text: The text of this RefusalMessage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and text is None:  # noqa: E501
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def link(self):
        """Gets the link of this RefusalMessage.  # noqa: E501

        Optional link that redirects to page associated with refusal reason.  # noqa: E501

        :return: The link of this RefusalMessage.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this RefusalMessage.

        Optional link that redirects to page associated with refusal reason.  # noqa: E501

        :param link: The link of this RefusalMessage.  # noqa: E501
        :type: str
        """

        self._link = link

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
        if not isinstance(other, RefusalMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RefusalMessage):
            return True

        return self.to_dict() != other.to_dict()