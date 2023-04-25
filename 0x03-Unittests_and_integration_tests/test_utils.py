#!/usr/bin/env python3
""" Parameterize a unit test """
from parameterized import parameterized
from unittest import mock
from unittest.mock import patch
import unittest

# Importing modules
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json


class TestAccessNestedMap(unittest.TestCase):
    """ Class that tests functions """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, end_results):
        """ Method that tests functions """
        self.assertEqual(access_nested_map(nested_map, path), end_results)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         end_exception):
        """ Testing invalid inputs that raises exception """
        with self.assertRaises(KeyError) as invalid:
            access_nested_map(nested_map, path)
        self.assertEqual(str(invalid.exception), end_exception)


class TestGetJson(unittest.TestCase):
    """ Class that tests get_json() method """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """Testing for the get_json() method"""
        with patch('requests.get') as get_response:

            get_response.return_value.json.return_value = payload
        # get_response.return_value = response
            result = get_json(url)
        # get_response.assert_called_once_with(url)
            self.assertEqual(result, payload)


if __name__ == '__main__':
    unittest.main()
