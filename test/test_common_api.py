# coding: utf-8

"""
    RESTful EPP

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.common_api import CommonApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCommonApi(unittest.TestCase):
    """CommonApi unit test stubs"""

    def setUp(self):
        self.api = CommonApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_messages_get(self):
        """Test case for messages_get

        Poll request  # noqa: E501
        """
        pass

    def test_messages_id_head(self):
        """Test case for messages_id_head

        Poll ack  # noqa: E501
        """
        pass

    def test_root_get(self):
        """Test case for root_get

        Hello  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
