#!/usr/bin/env python3

import unittest
from utils import access_nested_map
from utils import get_json
from parameterized import parameterized
from unittest.mock import MagicMock
from unittest.mock import patch
from utils import memoize
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
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")  
    def test_get_json(self, test_url, test_payload, mock_get):
      
        mock_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)  
        self.assertEqual(result, test_payload) 
        
class TestMemoize(unittest.TestCase):
 
 
    def test_memoize(self):
    
    
        class TestClass:
            def a_method(self):
                return 42

            @property
            @memoize
            def a_property(self):
                return self.a_method()

        test_instance = TestClass()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
            
if __name__ == '__main__':
    unittest.main()
