#!/usr/bin/env python3
"""Parameterize a unit test"""
from parameterized import parameterized
import unittest

access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Class that tests functions"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Method that tests functions"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    
if __name__ == '__main__':
    unittest.main()