#!/usr/bin/env python3

import unittest
from utils import access_nested_map
from utils import get_json
from parameterized import parameterized
from unittest.mock import MagicMock
from unittest.mock import patch
class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
    ])
    def test_access_nested_map_exception(self, nested_map, path, missing_key):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{missing_key}'")
       
       
class TestGetJson(unittest.TestCase):
   @parameterized.expand([
        (("example_true", "http://example.com", {"payload": True})),
        ("holberton_false", "http://holberton.io", {"payload": False}),
    ])
   @patch("requests.get")
   def test_get_json(self, name, url, test_payload, mock_get):
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(url), test_payload)

if __name__ == '__main__':
    unittest.main()
