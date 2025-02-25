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

class DomainTrnDataType(object):
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
        'ac_date': 'datetime',
        'ac_id': 'EppcomClIDType',
        'ex_date': 'datetime',
        'name': 'EppcomLabelType',
        're_date': 'datetime',
        're_id': 'EppcomClIDType',
        'tr_status': 'EppcomTrStatusType'
    }

    attribute_map = {
        'ac_date': 'acDate',
        'ac_id': 'acID',
        'ex_date': 'exDate',
        'name': 'name',
        're_date': 'reDate',
        're_id': 'reID',
        'tr_status': 'trStatus'
    }

    def __init__(self, ac_date=None, ac_id=None, ex_date=None, name=None, re_date=None, re_id=None, tr_status=None):  # noqa: E501
        """DomainTrnDataType - a model defined in Swagger"""  # noqa: E501
        self._ac_date = None
        self._ac_id = None
        self._ex_date = None
        self._name = None
        self._re_date = None
        self._re_id = None
        self._tr_status = None
        self.discriminator = None
        self.ac_date = ac_date
        self.ac_id = ac_id
        if ex_date is not None:
            self.ex_date = ex_date
        self.name = name
        self.re_date = re_date
        self.re_id = re_id
        self.tr_status = tr_status

    @property
    def ac_date(self):
        """Gets the ac_date of this DomainTrnDataType.  # noqa: E501


        :return: The ac_date of this DomainTrnDataType.  # noqa: E501
        :rtype: datetime
        """
        return self._ac_date

    @ac_date.setter
    def ac_date(self, ac_date):
        """Sets the ac_date of this DomainTrnDataType.


        :param ac_date: The ac_date of this DomainTrnDataType.  # noqa: E501
        :type: datetime
        """
        if ac_date is None:
            raise ValueError("Invalid value for `ac_date`, must not be `None`")  # noqa: E501

        self._ac_date = ac_date

    @property
    def ac_id(self):
        """Gets the ac_id of this DomainTrnDataType.  # noqa: E501


        :return: The ac_id of this DomainTrnDataType.  # noqa: E501
        :rtype: EppcomClIDType
        """
        return self._ac_id

    @ac_id.setter
    def ac_id(self, ac_id):
        """Sets the ac_id of this DomainTrnDataType.


        :param ac_id: The ac_id of this DomainTrnDataType.  # noqa: E501
        :type: EppcomClIDType
        """
        if ac_id is None:
            raise ValueError("Invalid value for `ac_id`, must not be `None`")  # noqa: E501

        self._ac_id = ac_id

    @property
    def ex_date(self):
        """Gets the ex_date of this DomainTrnDataType.  # noqa: E501


        :return: The ex_date of this DomainTrnDataType.  # noqa: E501
        :rtype: datetime
        """
        return self._ex_date

    @ex_date.setter
    def ex_date(self, ex_date):
        """Sets the ex_date of this DomainTrnDataType.


        :param ex_date: The ex_date of this DomainTrnDataType.  # noqa: E501
        :type: datetime
        """

        self._ex_date = ex_date

    @property
    def name(self):
        """Gets the name of this DomainTrnDataType.  # noqa: E501


        :return: The name of this DomainTrnDataType.  # noqa: E501
        :rtype: EppcomLabelType
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DomainTrnDataType.


        :param name: The name of this DomainTrnDataType.  # noqa: E501
        :type: EppcomLabelType
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def re_date(self):
        """Gets the re_date of this DomainTrnDataType.  # noqa: E501


        :return: The re_date of this DomainTrnDataType.  # noqa: E501
        :rtype: datetime
        """
        return self._re_date

    @re_date.setter
    def re_date(self, re_date):
        """Sets the re_date of this DomainTrnDataType.


        :param re_date: The re_date of this DomainTrnDataType.  # noqa: E501
        :type: datetime
        """
        if re_date is None:
            raise ValueError("Invalid value for `re_date`, must not be `None`")  # noqa: E501

        self._re_date = re_date

    @property
    def re_id(self):
        """Gets the re_id of this DomainTrnDataType.  # noqa: E501


        :return: The re_id of this DomainTrnDataType.  # noqa: E501
        :rtype: EppcomClIDType
        """
        return self._re_id

    @re_id.setter
    def re_id(self, re_id):
        """Sets the re_id of this DomainTrnDataType.


        :param re_id: The re_id of this DomainTrnDataType.  # noqa: E501
        :type: EppcomClIDType
        """
        if re_id is None:
            raise ValueError("Invalid value for `re_id`, must not be `None`")  # noqa: E501

        self._re_id = re_id

    @property
    def tr_status(self):
        """Gets the tr_status of this DomainTrnDataType.  # noqa: E501


        :return: The tr_status of this DomainTrnDataType.  # noqa: E501
        :rtype: EppcomTrStatusType
        """
        return self._tr_status

    @tr_status.setter
    def tr_status(self, tr_status):
        """Sets the tr_status of this DomainTrnDataType.


        :param tr_status: The tr_status of this DomainTrnDataType.  # noqa: E501
        :type: EppcomTrStatusType
        """
        if tr_status is None:
            raise ValueError("Invalid value for `tr_status`, must not be `None`")  # noqa: E501

        self._tr_status = tr_status

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
        if issubclass(DomainTrnDataType, dict):
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
        if not isinstance(other, DomainTrnDataType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
