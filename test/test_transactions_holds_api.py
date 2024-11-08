# coding: utf-8

"""
    Galileo Pro API Docs

    Galileo Pro Program API

    The version of the OpenAPI document: 1.0.0
    Contact: luis.reis@trustly.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.transactions_holds_api import TransactionsHoldsApi


class TestTransactionsHoldsApi(unittest.TestCase):
    """TransactionsHoldsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TransactionsHoldsApi()

    def tearDown(self) -> None:
        pass

    def test_create_hold_post(self) -> None:
        """Test case for create_hold_post

        Create Hold
        """
        pass

    def test_expire_hold_post(self) -> None:
        """Test case for expire_hold_post

        Expire Hold
        """
        pass

    def test_get_hold_history_post(self) -> None:
        """Test case for get_hold_history_post

        Get Hold History
        """
        pass


if __name__ == '__main__':
    unittest.main()
