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


class Publication(object):
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
        'ending_at': 'datetime',
        'starting_at': 'datetime',
        'status': 'str',
        'ended_by': 'str'
    }

    attribute_map = {
        'duration': 'duration',
        'ending_at': 'endingAt',
        'starting_at': 'startingAt',
        'status': 'status',
        'ended_by': 'endedBy'
    }

    def __init__(self, duration=None, ending_at=None, starting_at=None, status=None, ended_by=None):  # noqa: E501
        """Publication - a model defined in OpenAPI"""  # noqa: E501

        self._duration = None
        self._ending_at = None
        self._starting_at = None
        self._status = None
        self._ended_by = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if ending_at is not None:
            self.ending_at = ending_at
        if starting_at is not None:
            self.starting_at = starting_at
        if status is not None:
            self.status = status
        if ended_by is not None:
            self.ended_by = ended_by

    @property
    def duration(self):
        """Gets the duration of this Publication.  # noqa: E501

        Publication duration, ISO 8601 duration format  # noqa: E501

        :return: The duration of this Publication.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Publication.

        Publication duration, ISO 8601 duration format  # noqa: E501

        :param duration: The duration of this Publication.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def ending_at(self):
        """Gets the ending_at of this Publication.  # noqa: E501

        Publication ending date: Format (ISO 8601) - yyyy-MM-dd'T'HH:mm:ss.SSSZ. Cannot be modified  # noqa: E501

        :return: The ending_at of this Publication.  # noqa: E501
        :rtype: datetime
        """
        return self._ending_at

    @ending_at.setter
    def ending_at(self, ending_at):
        """Sets the ending_at of this Publication.

        Publication ending date: Format (ISO 8601) - yyyy-MM-dd'T'HH:mm:ss.SSSZ. Cannot be modified  # noqa: E501

        :param ending_at: The ending_at of this Publication.  # noqa: E501
        :type: datetime
        """

        self._ending_at = ending_at

    @property
    def starting_at(self):
        """Gets the starting_at of this Publication.  # noqa: E501

        Publication starting date: Format (ISO 8601) - yyyy-MM-dd'T'HH:mm:ss.SSSZ. Cannot be modified  # noqa: E501

        :return: The starting_at of this Publication.  # noqa: E501
        :rtype: datetime
        """
        return self._starting_at

    @starting_at.setter
    def starting_at(self, starting_at):
        """Sets the starting_at of this Publication.

        Publication starting date: Format (ISO 8601) - yyyy-MM-dd'T'HH:mm:ss.SSSZ. Cannot be modified  # noqa: E501

        :param starting_at: The starting_at of this Publication.  # noqa: E501
        :type: datetime
        """

        self._starting_at = starting_at

    @property
    def status(self):
        """Gets the status of this Publication.  # noqa: E501

        Publication status, one of: INACTIVE, ACTIVATING, ACTIVE, ENDED  # noqa: E501

        :return: The status of this Publication.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Publication.

        Publication status, one of: INACTIVE, ACTIVATING, ACTIVE, ENDED  # noqa: E501

        :param status: The status of this Publication.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def ended_by(self):
        """Gets the ended_by of this Publication.  # noqa: E501

        The types of ended by can be as follows:</br> - `USER` - offer ended by user.</br> - `ADMIN` - offer ended by admin.</br> - `EXPIRATION` - offer ended due to available items had sold out or offer duration had expired (valid for offers with specified duration).</br> - `ERROR` - offer ended due to internal problem with offer publication. The publication command responded with success status, but further processing failed.   # noqa: E501

        :return: The ended_by of this Publication.  # noqa: E501
        :rtype: str
        """
        return self._ended_by

    @ended_by.setter
    def ended_by(self, ended_by):
        """Sets the ended_by of this Publication.

        The types of ended by can be as follows:</br> - `USER` - offer ended by user.</br> - `ADMIN` - offer ended by admin.</br> - `EXPIRATION` - offer ended due to available items had sold out or offer duration had expired (valid for offers with specified duration).</br> - `ERROR` - offer ended due to internal problem with offer publication. The publication command responded with success status, but further processing failed.   # noqa: E501

        :param ended_by: The ended_by of this Publication.  # noqa: E501
        :type: str
        """
        allowed_values = ["USER", "ADMIN", "EXPIRATION", "ERROR"]  # noqa: E501
        if ended_by not in allowed_values:
            raise ValueError(
                "Invalid value for `ended_by` ({0}), must be one of {1}"  # noqa: E501
                .format(ended_by, allowed_values)
            )

        self._ended_by = ended_by

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
        if not isinstance(other, Publication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
