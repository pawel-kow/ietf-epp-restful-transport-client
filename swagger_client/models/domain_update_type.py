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

class DomainUpdateType(object):
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
        'add': 'DomainAddRemType',
        'chg': 'DomainChgType',
        'name': 'EppcomLabelType',
        'rem': 'DomainAddRemType'
    }

    attribute_map = {
        'add': 'add',
        'chg': 'chg',
        'name': 'name',
        'rem': 'rem'
    }

    def __init__(self, add=None, chg=None, name=None, rem=None):  # noqa: E501
        """DomainUpdateType - a model defined in Swagger"""  # noqa: E501
        self._add = None
        self._chg = None
        self._name = None
        self._rem = None
        self.discriminator = None
        if add is not None:
            self.add = add
        if chg is not None:
            self.chg = chg
        self.name = name
        if rem is not None:
            self.rem = rem

    @property
    def add(self):
        """Gets the add of this DomainUpdateType.  # noqa: E501


        :return: The add of this DomainUpdateType.  # noqa: E501
        :rtype: DomainAddRemType
        """
        return self._add

    @add.setter
    def add(self, add):
        """Sets the add of this DomainUpdateType.


        :param add: The add of this DomainUpdateType.  # noqa: E501
        :type: DomainAddRemType
        """

        self._add = add

    @property
    def chg(self):
        """Gets the chg of this DomainUpdateType.  # noqa: E501


        :return: The chg of this DomainUpdateType.  # noqa: E501
        :rtype: DomainChgType
        """
        return self._chg

    @chg.setter
    def chg(self, chg):
        """Sets the chg of this DomainUpdateType.


        :param chg: The chg of this DomainUpdateType.  # noqa: E501
        :type: DomainChgType
        """

        self._chg = chg

    @property
    def name(self):
        """Gets the name of this DomainUpdateType.  # noqa: E501


        :return: The name of this DomainUpdateType.  # noqa: E501
        :rtype: EppcomLabelType
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DomainUpdateType.


        :param name: The name of this DomainUpdateType.  # noqa: E501
        :type: EppcomLabelType
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def rem(self):
        """Gets the rem of this DomainUpdateType.  # noqa: E501


        :return: The rem of this DomainUpdateType.  # noqa: E501
        :rtype: DomainAddRemType
        """
        return self._rem

    @rem.setter
    def rem(self, rem):
        """Sets the rem of this DomainUpdateType.


        :param rem: The rem of this DomainUpdateType.  # noqa: E501
        :type: DomainAddRemType
        """

        self._rem = rem

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
        if issubclass(DomainUpdateType, dict):
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
        if not isinstance(other, DomainUpdateType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
