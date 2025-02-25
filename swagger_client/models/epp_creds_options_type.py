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

class EppCredsOptionsType(object):
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
        'lang': 'str',
        'version': 'EppVersionType'
    }

    attribute_map = {
        'lang': 'lang',
        'version': 'version'
    }

    def __init__(self, lang=None, version=None):  # noqa: E501
        """EppCredsOptionsType - a model defined in Swagger"""  # noqa: E501
        self._lang = None
        self._version = None
        self.discriminator = None
        self.lang = lang
        self.version = version

    @property
    def lang(self):
        """Gets the lang of this EppCredsOptionsType.  # noqa: E501


        :return: The lang of this EppCredsOptionsType.  # noqa: E501
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this EppCredsOptionsType.


        :param lang: The lang of this EppCredsOptionsType.  # noqa: E501
        :type: str
        """
        if lang is None:
            raise ValueError("Invalid value for `lang`, must not be `None`")  # noqa: E501

        self._lang = lang

    @property
    def version(self):
        """Gets the version of this EppCredsOptionsType.  # noqa: E501


        :return: The version of this EppCredsOptionsType.  # noqa: E501
        :rtype: EppVersionType
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this EppCredsOptionsType.


        :param version: The version of this EppCredsOptionsType.  # noqa: E501
        :type: EppVersionType
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

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
        if issubclass(EppCredsOptionsType, dict):
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
        if not isinstance(other, EppCredsOptionsType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
