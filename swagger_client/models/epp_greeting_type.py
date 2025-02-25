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

class EppGreetingType(object):
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
        'dcp': 'EppDcpType',
        'sv_date': 'datetime',
        'sv_id': 'EppSIDType',
        'svc_menu': 'EppSvcMenuType'
    }

    attribute_map = {
        'dcp': 'dcp',
        'sv_date': 'svDate',
        'sv_id': 'svID',
        'svc_menu': 'svcMenu'
    }

    def __init__(self, dcp=None, sv_date=None, sv_id=None, svc_menu=None):  # noqa: E501
        """EppGreetingType - a model defined in Swagger"""  # noqa: E501
        self._dcp = None
        self._sv_date = None
        self._sv_id = None
        self._svc_menu = None
        self.discriminator = None
        self.dcp = dcp
        self.sv_date = sv_date
        self.sv_id = sv_id
        self.svc_menu = svc_menu

    @property
    def dcp(self):
        """Gets the dcp of this EppGreetingType.  # noqa: E501


        :return: The dcp of this EppGreetingType.  # noqa: E501
        :rtype: EppDcpType
        """
        return self._dcp

    @dcp.setter
    def dcp(self, dcp):
        """Sets the dcp of this EppGreetingType.


        :param dcp: The dcp of this EppGreetingType.  # noqa: E501
        :type: EppDcpType
        """
        if dcp is None:
            raise ValueError("Invalid value for `dcp`, must not be `None`")  # noqa: E501

        self._dcp = dcp

    @property
    def sv_date(self):
        """Gets the sv_date of this EppGreetingType.  # noqa: E501


        :return: The sv_date of this EppGreetingType.  # noqa: E501
        :rtype: datetime
        """
        return self._sv_date

    @sv_date.setter
    def sv_date(self, sv_date):
        """Sets the sv_date of this EppGreetingType.


        :param sv_date: The sv_date of this EppGreetingType.  # noqa: E501
        :type: datetime
        """
        if sv_date is None:
            raise ValueError("Invalid value for `sv_date`, must not be `None`")  # noqa: E501

        self._sv_date = sv_date

    @property
    def sv_id(self):
        """Gets the sv_id of this EppGreetingType.  # noqa: E501


        :return: The sv_id of this EppGreetingType.  # noqa: E501
        :rtype: EppSIDType
        """
        return self._sv_id

    @sv_id.setter
    def sv_id(self, sv_id):
        """Sets the sv_id of this EppGreetingType.


        :param sv_id: The sv_id of this EppGreetingType.  # noqa: E501
        :type: EppSIDType
        """
        if sv_id is None:
            raise ValueError("Invalid value for `sv_id`, must not be `None`")  # noqa: E501

        self._sv_id = sv_id

    @property
    def svc_menu(self):
        """Gets the svc_menu of this EppGreetingType.  # noqa: E501


        :return: The svc_menu of this EppGreetingType.  # noqa: E501
        :rtype: EppSvcMenuType
        """
        return self._svc_menu

    @svc_menu.setter
    def svc_menu(self, svc_menu):
        """Sets the svc_menu of this EppGreetingType.


        :param svc_menu: The svc_menu of this EppGreetingType.  # noqa: E501
        :type: EppSvcMenuType
        """
        if svc_menu is None:
            raise ValueError("Invalid value for `svc_menu`, must not be `None`")  # noqa: E501

        self._svc_menu = svc_menu

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
        if issubclass(EppGreetingType, dict):
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
        if not isinstance(other, EppGreetingType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
