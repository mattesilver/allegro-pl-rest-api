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


class CheckoutFormDeliveryReference(object):
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
        'address': 'CheckoutFormDeliveryAddress',
        'method': 'CheckoutFormDeliveryMethod',
        'pickup_point': 'CheckoutFormDeliveryPickupPoint',
        'cost': 'Price',
        'time': 'CheckoutFormDeliveryTime',
        'smart': 'bool',
        'calculated_number_of_packages': 'int'
    }

    attribute_map = {
        'address': 'address',
        'method': 'method',
        'pickup_point': 'pickupPoint',
        'cost': 'cost',
        'time': 'time',
        'smart': 'smart',
        'calculated_number_of_packages': 'calculatedNumberOfPackages'
    }

    def __init__(self, address=None, method=None, pickup_point=None, cost=None, time=None, smart=None, calculated_number_of_packages=None, local_vars_configuration=None):  # noqa: E501
        """CheckoutFormDeliveryReference - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._method = None
        self._pickup_point = None
        self._cost = None
        self._time = None
        self._smart = None
        self._calculated_number_of_packages = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if method is not None:
            self.method = method
        if pickup_point is not None:
            self.pickup_point = pickup_point
        if cost is not None:
            self.cost = cost
        if time is not None:
            self.time = time
        if smart is not None:
            self.smart = smart
        if calculated_number_of_packages is not None:
            self.calculated_number_of_packages = calculated_number_of_packages

    @property
    def address(self):
        """Gets the address of this CheckoutFormDeliveryReference.  # noqa: E501


        :return: The address of this CheckoutFormDeliveryReference.  # noqa: E501
        :rtype: CheckoutFormDeliveryAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CheckoutFormDeliveryReference.


        :param address: The address of this CheckoutFormDeliveryReference.  # noqa: E501
        :type: CheckoutFormDeliveryAddress
        """

        self._address = address

    @property
    def method(self):
        """Gets the method of this CheckoutFormDeliveryReference.  # noqa: E501


        :return: The method of this CheckoutFormDeliveryReference.  # noqa: E501
        :rtype: CheckoutFormDeliveryMethod
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this CheckoutFormDeliveryReference.


        :param method: The method of this CheckoutFormDeliveryReference.  # noqa: E501
        :type: CheckoutFormDeliveryMethod
        """

        self._method = method

    @property
    def pickup_point(self):
        """Gets the pickup_point of this CheckoutFormDeliveryReference.  # noqa: E501


        :return: The pickup_point of this CheckoutFormDeliveryReference.  # noqa: E501
        :rtype: CheckoutFormDeliveryPickupPoint
        """
        return self._pickup_point

    @pickup_point.setter
    def pickup_point(self, pickup_point):
        """Sets the pickup_point of this CheckoutFormDeliveryReference.


        :param pickup_point: The pickup_point of this CheckoutFormDeliveryReference.  # noqa: E501
        :type: CheckoutFormDeliveryPickupPoint
        """

        self._pickup_point = pickup_point

    @property
    def cost(self):
        """Gets the cost of this CheckoutFormDeliveryReference.  # noqa: E501


        :return: The cost of this CheckoutFormDeliveryReference.  # noqa: E501
        :rtype: Price
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this CheckoutFormDeliveryReference.


        :param cost: The cost of this CheckoutFormDeliveryReference.  # noqa: E501
        :type: Price
        """

        self._cost = cost

    @property
    def time(self):
        """Gets the time of this CheckoutFormDeliveryReference.  # noqa: E501


        :return: The time of this CheckoutFormDeliveryReference.  # noqa: E501
        :rtype: CheckoutFormDeliveryTime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this CheckoutFormDeliveryReference.


        :param time: The time of this CheckoutFormDeliveryReference.  # noqa: E501
        :type: CheckoutFormDeliveryTime
        """

        self._time = time

    @property
    def smart(self):
        """Gets the smart of this CheckoutFormDeliveryReference.  # noqa: E501

        Buyer used a SMART option  # noqa: E501

        :return: The smart of this CheckoutFormDeliveryReference.  # noqa: E501
        :rtype: bool
        """
        return self._smart

    @smart.setter
    def smart(self, smart):
        """Sets the smart of this CheckoutFormDeliveryReference.

        Buyer used a SMART option  # noqa: E501

        :param smart: The smart of this CheckoutFormDeliveryReference.  # noqa: E501
        :type: bool
        """

        self._smart = smart

    @property
    def calculated_number_of_packages(self):
        """Gets the calculated_number_of_packages of this CheckoutFormDeliveryReference.  # noqa: E501

        Calculated number of packages.  # noqa: E501

        :return: The calculated_number_of_packages of this CheckoutFormDeliveryReference.  # noqa: E501
        :rtype: int
        """
        return self._calculated_number_of_packages

    @calculated_number_of_packages.setter
    def calculated_number_of_packages(self, calculated_number_of_packages):
        """Sets the calculated_number_of_packages of this CheckoutFormDeliveryReference.

        Calculated number of packages.  # noqa: E501

        :param calculated_number_of_packages: The calculated_number_of_packages of this CheckoutFormDeliveryReference.  # noqa: E501
        :type: int
        """

        self._calculated_number_of_packages = calculated_number_of_packages

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
        if not isinstance(other, CheckoutFormDeliveryReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CheckoutFormDeliveryReference):
            return True

        return self.to_dict() != other.to_dict()