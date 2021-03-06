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


class Validation(object):
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
        'errors': 'list[ValidationError]',
        'validated_at': 'datetime'
    }

    attribute_map = {
        'errors': 'errors',
        'validated_at': 'validatedAt'
    }

    def __init__(self, errors=None, validated_at=None, local_vars_configuration=None):  # noqa: E501
        """Validation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._errors = None
        self._validated_at = None
        self.discriminator = None

        self.errors = errors
        if validated_at is not None:
            self.validated_at = validated_at

    @property
    def errors(self):
        """Gets the errors of this Validation.  # noqa: E501


        :return: The errors of this Validation.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this Validation.


        :param errors: The errors of this Validation.  # noqa: E501
        :type: list[ValidationError]
        """
        if self.local_vars_configuration.client_side_validation and errors is None:  # noqa: E501
            raise ValueError("Invalid value for `errors`, must not be `None`")  # noqa: E501

        self._errors = errors

    @property
    def validated_at(self):
        """Gets the validated_at of this Validation.  # noqa: E501


        :return: The validated_at of this Validation.  # noqa: E501
        :rtype: datetime
        """
        return self._validated_at

    @validated_at.setter
    def validated_at(self, validated_at):
        """Sets the validated_at of this Validation.


        :param validated_at: The validated_at of this Validation.  # noqa: E501
        :type: datetime
        """

        self._validated_at = validated_at

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
        if not isinstance(other, Validation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Validation):
            return True

        return self.to_dict() != other.to_dict()
