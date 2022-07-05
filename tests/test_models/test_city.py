#!/usr/bin/python3
"""Unittest for User"""

import unittest
from models.city import City


class testCity(unittest.TestCase):
    """Test for City Class"""
    def test_str_stateid(self):
        """Check if state_id is a string"""
        self.assertEqual(str, type(City.state_id))

    def test_str_password(self):
        """Check if name is a string"""
        self.assertEqual(str, type(City.name))


if __name__ == '__main__':
    unittest.main()
