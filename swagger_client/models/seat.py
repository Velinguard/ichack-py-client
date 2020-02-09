# coding: utf-8

"""
    Api Documentation

    Api Documentation  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Seat(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'number': 'str',
        'taken': 'bool'
    }

    attribute_map = {
        'number': 'number',
        'taken': 'taken'
    }

    def __init__(self, number=None, taken=None):  # noqa: E501
        """Seat - a model defined in Swagger"""  # noqa: E501

        self._number = None
        self._taken = None
        self.discriminator = None

        if number is not None:
            self.number = number
        if taken is not None:
            self.taken = taken

    @property
    def number(self):
        """Gets the number of this Seat.  # noqa: E501


        :return: The number of this Seat.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Seat.


        :param number: The number of this Seat.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def taken(self):
        """Gets the taken of this Seat.  # noqa: E501


        :return: The taken of this Seat.  # noqa: E501
        :rtype: bool
        """
        return self._taken

    @taken.setter
    def taken(self, taken):
        """Sets the taken of this Seat.


        :param taken: The taken of this Seat.  # noqa: E501
        :type: bool
        """

        self._taken = taken

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Seat, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Seat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
