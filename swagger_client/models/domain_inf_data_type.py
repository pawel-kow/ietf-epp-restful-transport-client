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

class DomainInfDataType(object):
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
        'auth_info': 'DomainAuthInfoType',
        'cl_id': 'EppcomClIDType',
        'contact': 'list[DomainContactType]',
        'cr_date': 'datetime',
        'cr_id': 'EppcomClIDType',
        'ex_date': 'datetime',
        'host': 'list[EppcomLabelType]',
        'name': 'EppcomLabelType',
        'ns': 'DomainNsType',
        'registrant': 'EppcomClIDType',
        'roid': 'EppcomRoidType',
        'status': 'list[DomainStatusType]',
        'tr_date': 'datetime',
        'up_date': 'datetime',
        'up_id': 'EppcomClIDType'
    }

    attribute_map = {
        'auth_info': 'authInfo',
        'cl_id': 'clID',
        'contact': 'contact',
        'cr_date': 'crDate',
        'cr_id': 'crID',
        'ex_date': 'exDate',
        'host': 'host',
        'name': 'name',
        'ns': 'ns',
        'registrant': 'registrant',
        'roid': 'roid',
        'status': 'status',
        'tr_date': 'trDate',
        'up_date': 'upDate',
        'up_id': 'upID'
    }

    def __init__(self, auth_info=None, cl_id=None, contact=None, cr_date=None, cr_id=None, ex_date=None, host=None, name=None, ns=None, registrant=None, roid=None, status=None, tr_date=None, up_date=None, up_id=None):  # noqa: E501
        """DomainInfDataType - a model defined in Swagger"""  # noqa: E501
        self._auth_info = None
        self._cl_id = None
        self._contact = None
        self._cr_date = None
        self._cr_id = None
        self._ex_date = None
        self._host = None
        self._name = None
        self._ns = None
        self._registrant = None
        self._roid = None
        self._status = None
        self._tr_date = None
        self._up_date = None
        self._up_id = None
        self.discriminator = None
        if auth_info is not None:
            self.auth_info = auth_info
        self.cl_id = cl_id
        if contact is not None:
            self.contact = contact
        if cr_date is not None:
            self.cr_date = cr_date
        if cr_id is not None:
            self.cr_id = cr_id
        if ex_date is not None:
            self.ex_date = ex_date
        if host is not None:
            self.host = host
        self.name = name
        if ns is not None:
            self.ns = ns
        if registrant is not None:
            self.registrant = registrant
        self.roid = roid
        if status is not None:
            self.status = status
        if tr_date is not None:
            self.tr_date = tr_date
        if up_date is not None:
            self.up_date = up_date
        if up_id is not None:
            self.up_id = up_id

    @property
    def auth_info(self):
        """Gets the auth_info of this DomainInfDataType.  # noqa: E501


        :return: The auth_info of this DomainInfDataType.  # noqa: E501
        :rtype: DomainAuthInfoType
        """
        return self._auth_info

    @auth_info.setter
    def auth_info(self, auth_info):
        """Sets the auth_info of this DomainInfDataType.


        :param auth_info: The auth_info of this DomainInfDataType.  # noqa: E501
        :type: DomainAuthInfoType
        """

        self._auth_info = auth_info

    @property
    def cl_id(self):
        """Gets the cl_id of this DomainInfDataType.  # noqa: E501


        :return: The cl_id of this DomainInfDataType.  # noqa: E501
        :rtype: EppcomClIDType
        """
        return self._cl_id

    @cl_id.setter
    def cl_id(self, cl_id):
        """Sets the cl_id of this DomainInfDataType.


        :param cl_id: The cl_id of this DomainInfDataType.  # noqa: E501
        :type: EppcomClIDType
        """
        if cl_id is None:
            raise ValueError("Invalid value for `cl_id`, must not be `None`")  # noqa: E501

        self._cl_id = cl_id

    @property
    def contact(self):
        """Gets the contact of this DomainInfDataType.  # noqa: E501


        :return: The contact of this DomainInfDataType.  # noqa: E501
        :rtype: list[DomainContactType]
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this DomainInfDataType.


        :param contact: The contact of this DomainInfDataType.  # noqa: E501
        :type: list[DomainContactType]
        """

        self._contact = contact

    @property
    def cr_date(self):
        """Gets the cr_date of this DomainInfDataType.  # noqa: E501


        :return: The cr_date of this DomainInfDataType.  # noqa: E501
        :rtype: datetime
        """
        return self._cr_date

    @cr_date.setter
    def cr_date(self, cr_date):
        """Sets the cr_date of this DomainInfDataType.


        :param cr_date: The cr_date of this DomainInfDataType.  # noqa: E501
        :type: datetime
        """

        self._cr_date = cr_date

    @property
    def cr_id(self):
        """Gets the cr_id of this DomainInfDataType.  # noqa: E501


        :return: The cr_id of this DomainInfDataType.  # noqa: E501
        :rtype: EppcomClIDType
        """
        return self._cr_id

    @cr_id.setter
    def cr_id(self, cr_id):
        """Sets the cr_id of this DomainInfDataType.


        :param cr_id: The cr_id of this DomainInfDataType.  # noqa: E501
        :type: EppcomClIDType
        """

        self._cr_id = cr_id

    @property
    def ex_date(self):
        """Gets the ex_date of this DomainInfDataType.  # noqa: E501


        :return: The ex_date of this DomainInfDataType.  # noqa: E501
        :rtype: datetime
        """
        return self._ex_date

    @ex_date.setter
    def ex_date(self, ex_date):
        """Sets the ex_date of this DomainInfDataType.


        :param ex_date: The ex_date of this DomainInfDataType.  # noqa: E501
        :type: datetime
        """

        self._ex_date = ex_date

    @property
    def host(self):
        """Gets the host of this DomainInfDataType.  # noqa: E501


        :return: The host of this DomainInfDataType.  # noqa: E501
        :rtype: list[EppcomLabelType]
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this DomainInfDataType.


        :param host: The host of this DomainInfDataType.  # noqa: E501
        :type: list[EppcomLabelType]
        """

        self._host = host

    @property
    def name(self):
        """Gets the name of this DomainInfDataType.  # noqa: E501


        :return: The name of this DomainInfDataType.  # noqa: E501
        :rtype: EppcomLabelType
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DomainInfDataType.


        :param name: The name of this DomainInfDataType.  # noqa: E501
        :type: EppcomLabelType
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def ns(self):
        """Gets the ns of this DomainInfDataType.  # noqa: E501


        :return: The ns of this DomainInfDataType.  # noqa: E501
        :rtype: DomainNsType
        """
        return self._ns

    @ns.setter
    def ns(self, ns):
        """Sets the ns of this DomainInfDataType.


        :param ns: The ns of this DomainInfDataType.  # noqa: E501
        :type: DomainNsType
        """

        self._ns = ns

    @property
    def registrant(self):
        """Gets the registrant of this DomainInfDataType.  # noqa: E501


        :return: The registrant of this DomainInfDataType.  # noqa: E501
        :rtype: EppcomClIDType
        """
        return self._registrant

    @registrant.setter
    def registrant(self, registrant):
        """Sets the registrant of this DomainInfDataType.


        :param registrant: The registrant of this DomainInfDataType.  # noqa: E501
        :type: EppcomClIDType
        """

        self._registrant = registrant

    @property
    def roid(self):
        """Gets the roid of this DomainInfDataType.  # noqa: E501


        :return: The roid of this DomainInfDataType.  # noqa: E501
        :rtype: EppcomRoidType
        """
        return self._roid

    @roid.setter
    def roid(self, roid):
        """Sets the roid of this DomainInfDataType.


        :param roid: The roid of this DomainInfDataType.  # noqa: E501
        :type: EppcomRoidType
        """
        if roid is None:
            raise ValueError("Invalid value for `roid`, must not be `None`")  # noqa: E501

        self._roid = roid

    @property
    def status(self):
        """Gets the status of this DomainInfDataType.  # noqa: E501


        :return: The status of this DomainInfDataType.  # noqa: E501
        :rtype: list[DomainStatusType]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DomainInfDataType.


        :param status: The status of this DomainInfDataType.  # noqa: E501
        :type: list[DomainStatusType]
        """

        self._status = status

    @property
    def tr_date(self):
        """Gets the tr_date of this DomainInfDataType.  # noqa: E501


        :return: The tr_date of this DomainInfDataType.  # noqa: E501
        :rtype: datetime
        """
        return self._tr_date

    @tr_date.setter
    def tr_date(self, tr_date):
        """Sets the tr_date of this DomainInfDataType.


        :param tr_date: The tr_date of this DomainInfDataType.  # noqa: E501
        :type: datetime
        """

        self._tr_date = tr_date

    @property
    def up_date(self):
        """Gets the up_date of this DomainInfDataType.  # noqa: E501


        :return: The up_date of this DomainInfDataType.  # noqa: E501
        :rtype: datetime
        """
        return self._up_date

    @up_date.setter
    def up_date(self, up_date):
        """Sets the up_date of this DomainInfDataType.


        :param up_date: The up_date of this DomainInfDataType.  # noqa: E501
        :type: datetime
        """

        self._up_date = up_date

    @property
    def up_id(self):
        """Gets the up_id of this DomainInfDataType.  # noqa: E501


        :return: The up_id of this DomainInfDataType.  # noqa: E501
        :rtype: EppcomClIDType
        """
        return self._up_id

    @up_id.setter
    def up_id(self, up_id):
        """Sets the up_id of this DomainInfDataType.


        :param up_id: The up_id of this DomainInfDataType.  # noqa: E501
        :type: EppcomClIDType
        """

        self._up_id = up_id

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
        if issubclass(DomainInfDataType, dict):
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
        if not isinstance(other, DomainInfDataType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
