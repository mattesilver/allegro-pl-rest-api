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


class InlineResponse2001DeliveryMethods(object):
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
        'name': 'str',
        'payment_policy': 'str',
        'allegro_endorsed': 'bool',
        'shipping_rates_constraints': 'InlineResponse2001ShippingRatesConstraints'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'payment_policy': 'paymentPolicy',
        'allegro_endorsed': 'allegroEndorsed',
        'shipping_rates_constraints': 'shippingRatesConstraints'
    }

    def __init__(self, id=None, name=None, payment_policy=None, allegro_endorsed=None, shipping_rates_constraints=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse2001DeliveryMethods - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._payment_policy = None
        self._allegro_endorsed = None
        self._shipping_rates_constraints = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if payment_policy is not None:
            self.payment_policy = payment_policy
        if allegro_endorsed is not None:
            self.allegro_endorsed = allegro_endorsed
        if shipping_rates_constraints is not None:
            self.shipping_rates_constraints = shipping_rates_constraints

    @property
    def id(self):
        """Gets the id of this InlineResponse2001DeliveryMethods.  # noqa: E501

        Delivery method ID.  # noqa: E501

        :return: The id of this InlineResponse2001DeliveryMethods.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2001DeliveryMethods.

        Delivery method ID.  # noqa: E501

        :param id: The id of this InlineResponse2001DeliveryMethods.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse2001DeliveryMethods.  # noqa: E501

        Delivery method name.  # noqa: E501

        :return: The name of this InlineResponse2001DeliveryMethods.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2001DeliveryMethods.

        Delivery method name.  # noqa: E501

        :param name: The name of this InlineResponse2001DeliveryMethods.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def payment_policy(self):
        """Gets the payment_policy of this InlineResponse2001DeliveryMethods.  # noqa: E501

        Whether the payment is to be collected in advance or on delivery.  # noqa: E501

        :return: The payment_policy of this InlineResponse2001DeliveryMethods.  # noqa: E501
        :rtype: str
        """
        return self._payment_policy

    @payment_policy.setter
    def payment_policy(self, payment_policy):
        """Sets the payment_policy of this InlineResponse2001DeliveryMethods.

        Whether the payment is to be collected in advance or on delivery.  # noqa: E501

        :param payment_policy: The payment_policy of this InlineResponse2001DeliveryMethods.  # noqa: E501
        :type: str
        """
        allowed_values = ["IN_ADVANCE", "CASH_ON_DELIVERY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and payment_policy not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `payment_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(payment_policy, allowed_values)
            )

        self._payment_policy = payment_policy

    @property
    def allegro_endorsed(self):
        """Gets the allegro_endorsed of this InlineResponse2001DeliveryMethods.  # noqa: E501

        Indicates Allegro signed delivery method, which allows to easily distinguish similar delivery methods with various restrictions, e.g. Allegro Paczkomaty 24/7 InPost from Paczkomaty 24/7.  # noqa: E501

        :return: The allegro_endorsed of this InlineResponse2001DeliveryMethods.  # noqa: E501
        :rtype: bool
        """
        return self._allegro_endorsed

    @allegro_endorsed.setter
    def allegro_endorsed(self, allegro_endorsed):
        """Sets the allegro_endorsed of this InlineResponse2001DeliveryMethods.

        Indicates Allegro signed delivery method, which allows to easily distinguish similar delivery methods with various restrictions, e.g. Allegro Paczkomaty 24/7 InPost from Paczkomaty 24/7.  # noqa: E501

        :param allegro_endorsed: The allegro_endorsed of this InlineResponse2001DeliveryMethods.  # noqa: E501
        :type: bool
        """

        self._allegro_endorsed = allegro_endorsed

    @property
    def shipping_rates_constraints(self):
        """Gets the shipping_rates_constraints of this InlineResponse2001DeliveryMethods.  # noqa: E501


        :return: The shipping_rates_constraints of this InlineResponse2001DeliveryMethods.  # noqa: E501
        :rtype: InlineResponse2001ShippingRatesConstraints
        """
        return self._shipping_rates_constraints

    @shipping_rates_constraints.setter
    def shipping_rates_constraints(self, shipping_rates_constraints):
        """Sets the shipping_rates_constraints of this InlineResponse2001DeliveryMethods.


        :param shipping_rates_constraints: The shipping_rates_constraints of this InlineResponse2001DeliveryMethods.  # noqa: E501
        :type: InlineResponse2001ShippingRatesConstraints
        """

        self._shipping_rates_constraints = shipping_rates_constraints

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
        if not isinstance(other, InlineResponse2001DeliveryMethods):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2001DeliveryMethods):
            return True

        return self.to_dict() != other.to_dict()