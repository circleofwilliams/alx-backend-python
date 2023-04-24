#!/usr/bin/env python3
"""test_utils module
"""
import unittest
import requests
from unittest.mock import patch
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json


class TestAccessNestedMap(unittest.TestCase):
    """An access_nested_map function test class"""
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
#    def test_access_nested_map(self, nested_map, path, expected):
#        """Test to access nested map with key path.
#        Parameters
#        ----------
#            nested_map: A nested map
#            path: A sequence of key representing a path to the value
#            expected: Expected result from the function
#        """
#        self.assertEqual(access_nested_map(nested_map, path), expected)

    def test_access_nested_map_exception(self, nested_map, path):
        """Test for an Exception to access nested map with key path.
        Parameters
        ----------
            nested_map: A nested map
            path: A sequence of key representing a path to the value
            expected: Expected result from the function
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """A get_json function test class
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, expected):
        """Test for an Exception to access nested map with key path.
        Parameters
        ----------
            test_url: A test url
            expected: Expected result from the function
        """
        with patch('utils.requests') as mock:
            mock.get.return_value.json.return_value = expected
            res = get_json(test_url)
            self.assertEqual(res, expected)
            mock.get.assert_called_once()
