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


class BuyerReference(object):
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
        'email': 'str',
        'login': 'str',
        'guest': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'email': 'email',
        'login': 'login',
        'guest': 'guest'
    }

    def __init__(self, id=None, email=None, login=None, guest=None, local_vars_configuration=None):  # noqa: E501
        """BuyerReference - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._email = None
        self._login = None
        self._guest = None
        self.discriminator = None

        self.id = id
        self.email = email
        self.login = login
        self.guest = guest

    @property
    def id(self):
        """Gets the id of this BuyerReference.  # noqa: E501

        buyer id  # noqa: E501

        :return: The id of this BuyerReference.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BuyerReference.

        buyer id  # noqa: E501

        :param id: The id of this BuyerReference.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def email(self):
        """Gets the email of this BuyerReference.  # noqa: E501


        :return: The email of this BuyerReference.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BuyerReference.


        :param email: The email of this BuyerReference.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def login(self):
        """Gets the login of this BuyerReference.  # noqa: E501


        :return: The login of this BuyerReference.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this BuyerReference.


        :param login: The login of this BuyerReference.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and login is None:  # noqa: E501
            raise ValueError("Invalid value for `login`, must not be `None`")  # noqa: E501

        self._login = login

    @property
    def guest(self):
        """Gets the guest of this BuyerReference.  # noqa: E501

        is a guest account?  # noqa: E501

        :return: The guest of this BuyerReference.  # noqa: E501
        :rtype: bool
        """
        return self._guest

    @guest.setter
    def guest(self, guest):
        """Sets the guest of this BuyerReference.

        is a guest account?  # noqa: E501

        :param guest: The guest of this BuyerReference.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and guest is None:  # noqa: E501
            raise ValueError("Invalid value for `guest`, must not be `None`")  # noqa: E501

        self._guest = guest

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
        if not isinstance(other, BuyerReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BuyerReference):
            return True

        return self.to_dict() != other.to_dict()
