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
from swagger_client.models.epp_epp_type import EppEppType  # noqa: F401,E501

class DomainCreateRequest(EppEppType):
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
        'command': 'DomainCreateRequestCommand'
    }
    if hasattr(EppEppType, "swagger_types"):
        swagger_types.update(EppEppType.swagger_types)

    attribute_map = {
        'command': 'command'
    }
    if hasattr(EppEppType, "attribute_map"):
        attribute_map.update(EppEppType.attribute_map)

    def __init__(self, command=None, *args, **kwargs):  # noqa: E501
        """DomainCreateRequest - a model defined in Swagger"""  # noqa: E501
        self._command = None
        self.discriminator = None
        self.command = command
        EppEppType.__init__(self, *args, **kwargs)

    @property
    def command(self):
        """Gets the command of this DomainCreateRequest.  # noqa: E501


        :return: The command of this DomainCreateRequest.  # noqa: E501
        :rtype: DomainCreateRequestCommand
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this DomainCreateRequest.


        :param command: The command of this DomainCreateRequest.  # noqa: E501
        :type: DomainCreateRequestCommand
        """
        if command is None:
            raise ValueError("Invalid value for `command`, must not be `None`")  # noqa: E501

        self._command = command

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
        if issubclass(DomainCreateRequest, dict):
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
        if not isinstance(other, DomainCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
