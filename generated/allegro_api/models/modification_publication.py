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


class ModificationPublication(object):
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
        'duration': 'str',
        'duration_unlimited': 'bool'
    }

    attribute_map = {
        'duration': 'duration',
        'duration_unlimited': 'durationUnlimited'
    }

    def __init__(self, duration=None, duration_unlimited=None, local_vars_configuration=None):  # noqa: E501
        """ModificationPublication - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._duration = None
        self._duration_unlimited = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if duration_unlimited is not None:
            self.duration_unlimited = duration_unlimited

    @property
    def duration(self):
        """Gets the duration of this ModificationPublication.  # noqa: E501

        Offer duration time provided in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.  # noqa: E501

        :return: The duration of this ModificationPublication.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ModificationPublication.

        Offer duration time provided in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.  # noqa: E501

        :param duration: The duration of this ModificationPublication.  # noqa: E501
        :type: str
        """
        allowed_values = ["PT72H", "PT120H", "PT168H", "PT240H", "PT480H", "PT720H", "P3D", "P5D", "P7D", "P10D", "P20D", "P30D"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and duration not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `duration` ({0}), must be one of {1}"  # noqa: E501
                .format(duration, allowed_values)
            )

        self._duration = duration

    @property
    def duration_unlimited(self):
        """Gets the duration_unlimited of this ModificationPublication.  # noqa: E501

        Unlimited duration time.  # noqa: E501

        :return: The duration_unlimited of this ModificationPublication.  # noqa: E501
        :rtype: bool
        """
        return self._duration_unlimited

    @duration_unlimited.setter
    def duration_unlimited(self, duration_unlimited):
        """Sets the duration_unlimited of this ModificationPublication.

        Unlimited duration time.  # noqa: E501

        :param duration_unlimited: The duration_unlimited of this ModificationPublication.  # noqa: E501
        :type: bool
        """

        self._duration_unlimited = duration_unlimited

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
        if not isinstance(other, ModificationPublication):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModificationPublication):
            return True

        return self.to_dict() != other.to_dict()
