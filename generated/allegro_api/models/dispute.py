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


class Dispute(object):
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
        'subject': 'Subject',
        'status': 'str',
        'buyer': 'DisputeUser',
        'seller': 'DisputeUser',
        'checkout_form': 'DisputeCheckoutForm',
        'message': 'DisputeFirstMessage',
        'messages_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'subject': 'subject',
        'status': 'status',
        'buyer': 'buyer',
        'seller': 'seller',
        'checkout_form': 'checkoutForm',
        'message': 'message',
        'messages_count': 'messagesCount'
    }

    def __init__(self, id=None, subject=None, status=None, buyer=None, seller=None, checkout_form=None, message=None, messages_count=None, local_vars_configuration=None):  # noqa: E501
        """Dispute - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._subject = None
        self._status = None
        self._buyer = None
        self._seller = None
        self._checkout_form = None
        self._message = None
        self._messages_count = None
        self.discriminator = None

        self.id = id
        self.subject = subject
        self.status = status
        self.buyer = buyer
        self.seller = seller
        self.checkout_form = checkout_form
        self.message = message
        self.messages_count = messages_count

    @property
    def id(self):
        """Gets the id of this Dispute.  # noqa: E501

        Identifier of the dispute  # noqa: E501

        :return: The id of this Dispute.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Dispute.

        Identifier of the dispute  # noqa: E501

        :param id: The id of this Dispute.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def subject(self):
        """Gets the subject of this Dispute.  # noqa: E501


        :return: The subject of this Dispute.  # noqa: E501
        :rtype: Subject
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this Dispute.


        :param subject: The subject of this Dispute.  # noqa: E501
        :type: Subject
        """
        if self.local_vars_configuration.client_side_validation and subject is None:  # noqa: E501
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

    @property
    def status(self):
        """Gets the status of this Dispute.  # noqa: E501


        :return: The status of this Dispute.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Dispute.


        :param status: The status of this Dispute.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["CLOSED", "ONGOING", "UNRESOLVED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def buyer(self):
        """Gets the buyer of this Dispute.  # noqa: E501


        :return: The buyer of this Dispute.  # noqa: E501
        :rtype: DisputeUser
        """
        return self._buyer

    @buyer.setter
    def buyer(self, buyer):
        """Sets the buyer of this Dispute.


        :param buyer: The buyer of this Dispute.  # noqa: E501
        :type: DisputeUser
        """
        if self.local_vars_configuration.client_side_validation and buyer is None:  # noqa: E501
            raise ValueError("Invalid value for `buyer`, must not be `None`")  # noqa: E501

        self._buyer = buyer

    @property
    def seller(self):
        """Gets the seller of this Dispute.  # noqa: E501


        :return: The seller of this Dispute.  # noqa: E501
        :rtype: DisputeUser
        """
        return self._seller

    @seller.setter
    def seller(self, seller):
        """Sets the seller of this Dispute.


        :param seller: The seller of this Dispute.  # noqa: E501
        :type: DisputeUser
        """
        if self.local_vars_configuration.client_side_validation and seller is None:  # noqa: E501
            raise ValueError("Invalid value for `seller`, must not be `None`")  # noqa: E501

        self._seller = seller

    @property
    def checkout_form(self):
        """Gets the checkout_form of this Dispute.  # noqa: E501


        :return: The checkout_form of this Dispute.  # noqa: E501
        :rtype: DisputeCheckoutForm
        """
        return self._checkout_form

    @checkout_form.setter
    def checkout_form(self, checkout_form):
        """Sets the checkout_form of this Dispute.


        :param checkout_form: The checkout_form of this Dispute.  # noqa: E501
        :type: DisputeCheckoutForm
        """
        if self.local_vars_configuration.client_side_validation and checkout_form is None:  # noqa: E501
            raise ValueError("Invalid value for `checkout_form`, must not be `None`")  # noqa: E501

        self._checkout_form = checkout_form

    @property
    def message(self):
        """Gets the message of this Dispute.  # noqa: E501


        :return: The message of this Dispute.  # noqa: E501
        :rtype: DisputeFirstMessage
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Dispute.


        :param message: The message of this Dispute.  # noqa: E501
        :type: DisputeFirstMessage
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def messages_count(self):
        """Gets the messages_count of this Dispute.  # noqa: E501


        :return: The messages_count of this Dispute.  # noqa: E501
        :rtype: int
        """
        return self._messages_count

    @messages_count.setter
    def messages_count(self, messages_count):
        """Sets the messages_count of this Dispute.


        :param messages_count: The messages_count of this Dispute.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and messages_count is None:  # noqa: E501
            raise ValueError("Invalid value for `messages_count`, must not be `None`")  # noqa: E501

        self._messages_count = messages_count

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
        if not isinstance(other, Dispute):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Dispute):
            return True

        return self.to_dict() != other.to_dict()
