# coding: utf-8

"""
    RESTful EPP

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class HostCheckType(object):
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
        'name': 'HostCheckNameType',
        'reason': 'EppcomReasonType'
    }

    attribute_map = {
        'name': 'name',
        'reason': 'reason'
    }

    def __init__(self, name=None, reason=None):  # noqa: E501
        """HostCheckType - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._reason = None
        self.discriminator = None
        self.name = name
        if reason is not None:
            self.reason = reason

    @property
    def name(self):
        """Gets the name of this HostCheckType.  # noqa: E501


        :return: The name of this HostCheckType.  # noqa: E501
        :rtype: HostCheckNameType
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HostCheckType.


        :param name: The name of this HostCheckType.  # noqa: E501
        :type: HostCheckNameType
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def reason(self):
        """Gets the reason of this HostCheckType.  # noqa: E501


        :return: The reason of this HostCheckType.  # noqa: E501
        :rtype: EppcomReasonType
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this HostCheckType.


        :param reason: The reason of this HostCheckType.  # noqa: E501
        :type: EppcomReasonType
        """

        self._reason = reason

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
        if issubclass(HostCheckType, dict):
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
        if not isinstance(other, HostCheckType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
