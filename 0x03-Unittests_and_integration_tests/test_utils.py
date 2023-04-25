#!/usr/bin/env python3
"""test_utils module
"""
import unittest
import requests
from unittest.mock import patch
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


class TestAccessNestedMap(unittest.TestCase):
    """An access_nested_map function test class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test to access nested map with key path.
        Parameters
        ----------
            nested_map: A nested map
            path: A sequence of key representing a path to the value
            expected: Expected result from the function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


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
        """Test for get_json function with test url.
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


class TestMemoize(unittest.TestCase):
    """A memoize function test class
    """
    @parameterized.expand([
        (42, ),
        (42, ),
    ])
    def test_memoize(self, expected):
        """Test for an Exception to access nested map with key path.
        Parameters
        ----------
            test_url: A test url
            expected: Expected result from the function
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch('TestClass.a_method') as mock:
            res = [TestClass.a_property(), TestClass.a_property()]
            self.assertEqual(res, result)
            mock.assert_called_once()
