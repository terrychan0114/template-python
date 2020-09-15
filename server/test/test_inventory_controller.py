# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from server.models.inventory_info import InventoryInfo  # noqa: E501
from server.test import BaseTestCase


class TestInventoryController(BaseTestCase):
    """InventoryController integration test stubs"""

    def test_add_pn(self):
        """Test case for add_pn

        Add a new work order to the server
        """
        body = InventoryInfo()
        response = self.client.open(
            '/inventory',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_inv(self):
        """Test case for get_inv

        Get the information of all inventory
        """
        response = self.client.open(
            '/inventory',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ln(self):
        """Test case for get_ln

        Get the information of a lot number
        """
        query_string = [('lot_number', 'lot_number_example')]
        response = self.client.open(
            '/inventory/lot-number',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_pn(self):
        """Test case for get_pn

        Get the information of a part number
        """
        query_string = [('part_number', 'part_number_example')]
        response = self.client.open(
            '/inventory/part-number',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_pn(self):
        """Test case for update_pn

        Update a part number
        """
        body = InventoryInfo()
        response = self.client.open(
            '/inventory',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
