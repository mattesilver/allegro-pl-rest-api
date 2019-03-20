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


class Pos(object):
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
        'external_id': 'str',
        'name': 'str',
        'seller': 'Seller',
        'type': 'str',
        'address': 'Address',
        'phone_number': 'str',
        'email': 'str',
        'open_hours': 'list[OpenHour]',
        'service_time': 'str',
        'payments': 'list[Payment]',
        'confirmation_type': 'str',
        'status': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'external_id': 'externalId',
        'name': 'name',
        'seller': 'seller',
        'type': 'type',
        'address': 'address',
        'phone_number': 'phoneNumber',
        'email': 'email',
        'open_hours': 'openHours',
        'service_time': 'serviceTime',
        'payments': 'payments',
        'confirmation_type': 'confirmationType',
        'status': 'status',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt'
    }

    def __init__(self, id=None, external_id=None, name=None, seller=None, type=None, address=None, phone_number=None, email=None, open_hours=None, service_time=None, payments=None, confirmation_type=None, status=None, created_at=None, updated_at=None):  # noqa: E501
        """Pos - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._external_id = None
        self._name = None
        self._seller = None
        self._type = None
        self._address = None
        self._phone_number = None
        self._email = None
        self._open_hours = None
        self._service_time = None
        self._payments = None
        self._confirmation_type = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if external_id is not None:
            self.external_id = external_id
        self.name = name
        if seller is not None:
            self.seller = seller
        self.type = type
        self.address = address
        if phone_number is not None:
            self.phone_number = phone_number
        if email is not None:
            self.email = email
        self.open_hours = open_hours
        if service_time is not None:
            self.service_time = service_time
        if payments is not None:
            self.payments = payments
        self.confirmation_type = confirmation_type
        self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Pos.  # noqa: E501

        UUID. When creating a point of service (Post) the field is ignored. It is required when updating (Put) a point of service.  # noqa: E501

        :return: The id of this Pos.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Pos.

        UUID. When creating a point of service (Post) the field is ignored. It is required when updating (Put) a point of service.  # noqa: E501

        :param id: The id of this Pos.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def external_id(self):
        """Gets the external_id of this Pos.  # noqa: E501

        ID from external client system.  # noqa: E501

        :return: The external_id of this Pos.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Pos.

        ID from external client system.  # noqa: E501

        :param external_id: The external_id of this Pos.  # noqa: E501
        :type: str
        """
        if external_id is not None and len(external_id) > 80:
            raise ValueError("Invalid value for `external_id`, length must be less than or equal to `80`")  # noqa: E501

        self._external_id = external_id

    @property
    def name(self):
        """Gets the name of this Pos.  # noqa: E501


        :return: The name of this Pos.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Pos.


        :param name: The name of this Pos.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 80:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `80`")  # noqa: E501

        self._name = name

    @property
    def seller(self):
        """Gets the seller of this Pos.  # noqa: E501


        :return: The seller of this Pos.  # noqa: E501
        :rtype: Seller
        """
        return self._seller

    @seller.setter
    def seller(self, seller):
        """Sets the seller of this Pos.


        :param seller: The seller of this Pos.  # noqa: E501
        :type: Seller
        """

        self._seller = seller

    @property
    def type(self):
        """Gets the type of this Pos.  # noqa: E501

        Indicates point type. The only valid value so far is PICKUP_POINT.  # noqa: E501

        :return: The type of this Pos.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Pos.

        Indicates point type. The only valid value so far is PICKUP_POINT.  # noqa: E501

        :param type: The type of this Pos.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def address(self):
        """Gets the address of this Pos.  # noqa: E501


        :return: The address of this Pos.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Pos.


        :param address: The address of this Pos.  # noqa: E501
        :type: Address
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def phone_number(self):
        """Gets the phone_number of this Pos.  # noqa: E501


        :return: The phone_number of this Pos.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this Pos.


        :param phone_number: The phone_number of this Pos.  # noqa: E501
        :type: str
        """
        if phone_number is not None and len(phone_number) > 16:
            raise ValueError("Invalid value for `phone_number`, length must be less than or equal to `16`")  # noqa: E501

        self._phone_number = phone_number

    @property
    def email(self):
        """Gets the email of this Pos.  # noqa: E501


        :return: The email of this Pos.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Pos.


        :param email: The email of this Pos.  # noqa: E501
        :type: str
        """
        if email is not None and len(email) > 64:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `64`")  # noqa: E501

        self._email = email

    @property
    def open_hours(self):
        """Gets the open_hours of this Pos.  # noqa: E501

        Possible empty list of opening hours.  # noqa: E501

        :return: The open_hours of this Pos.  # noqa: E501
        :rtype: list[OpenHour]
        """
        return self._open_hours

    @open_hours.setter
    def open_hours(self, open_hours):
        """Sets the open_hours of this Pos.

        Possible empty list of opening hours.  # noqa: E501

        :param open_hours: The open_hours of this Pos.  # noqa: E501
        :type: list[OpenHour]
        """
        if open_hours is None:
            raise ValueError("Invalid value for `open_hours`, must not be `None`")  # noqa: E501

        self._open_hours = open_hours

    @property
    def service_time(self):
        """Gets the service_time of this Pos.  # noqa: E501

        Delivery time / Time period for receipt. Date format ISO 8601 e.g. 'PT24H'  # noqa: E501

        :return: The service_time of this Pos.  # noqa: E501
        :rtype: str
        """
        return self._service_time

    @service_time.setter
    def service_time(self, service_time):
        """Sets the service_time of this Pos.

        Delivery time / Time period for receipt. Date format ISO 8601 e.g. 'PT24H'  # noqa: E501

        :param service_time: The service_time of this Pos.  # noqa: E501
        :type: str
        """

        self._service_time = service_time

    @property
    def payments(self):
        """Gets the payments of this Pos.  # noqa: E501

        An empty list of payment types is available.  # noqa: E501

        :return: The payments of this Pos.  # noqa: E501
        :rtype: list[Payment]
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """Sets the payments of this Pos.

        An empty list of payment types is available.  # noqa: E501

        :param payments: The payments of this Pos.  # noqa: E501
        :type: list[Payment]
        """

        self._payments = payments

    @property
    def confirmation_type(self):
        """Gets the confirmation_type of this Pos.  # noqa: E501

        Confirmation method: AWAIT_CONTACT - We will inform you about the time of receipt, CALL_US - Please make an appointment, CONTACT_NOT_REQUIRED - Contact is not required.  # noqa: E501

        :return: The confirmation_type of this Pos.  # noqa: E501
        :rtype: str
        """
        return self._confirmation_type

    @confirmation_type.setter
    def confirmation_type(self, confirmation_type):
        """Sets the confirmation_type of this Pos.

        Confirmation method: AWAIT_CONTACT - We will inform you about the time of receipt, CALL_US - Please make an appointment, CONTACT_NOT_REQUIRED - Contact is not required.  # noqa: E501

        :param confirmation_type: The confirmation_type of this Pos.  # noqa: E501
        :type: str
        """
        if confirmation_type is None:
            raise ValueError("Invalid value for `confirmation_type`, must not be `None`")  # noqa: E501

        self._confirmation_type = confirmation_type

    @property
    def status(self):
        """Gets the status of this Pos.  # noqa: E501

        Point of service status: ACTIVE - active, TEMPORARILY_CLOSED - temporarily closed, CLOSED_DOWN - closed down, DELETED - deleted.  # noqa: E501

        :return: The status of this Pos.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Pos.

        Point of service status: ACTIVE - active, TEMPORARILY_CLOSED - temporarily closed, CLOSED_DOWN - closed down, DELETED - deleted.  # noqa: E501

        :param status: The status of this Pos.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this Pos.  # noqa: E501

        Creation date. Date format (ISO 8601) - yyyy-MM-dd'T'HH:mm:ss.SSSZ  # noqa: E501

        :return: The created_at of this Pos.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Pos.

        Creation date. Date format (ISO 8601) - yyyy-MM-dd'T'HH:mm:ss.SSSZ  # noqa: E501

        :param created_at: The created_at of this Pos.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Pos.  # noqa: E501

        Modification date. Date format (ISO 8601) - yyyy-MM-dd'T'HH:mm:ss.SSSZ  # noqa: E501

        :return: The updated_at of this Pos.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Pos.

        Modification date. Date format (ISO 8601) - yyyy-MM-dd'T'HH:mm:ss.SSSZ  # noqa: E501

        :param updated_at: The updated_at of this Pos.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if not isinstance(other, Pos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other