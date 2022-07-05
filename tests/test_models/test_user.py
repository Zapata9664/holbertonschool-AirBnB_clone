#!/usr/bin/python3
"""Unittest for User"""

import unittest
from models.user import User


class testUser(unittest.TestCase):
    """Test for User Class"""
    def test_str_email(self):
        """Check if email is a string"""
        self.assertEqual(str, type(User.email))

    def test_str_password(self):
        """Check if password is a string"""
        self.assertEqual(str, type(User.password))

    def test_str_first_name(self):
        """Check if first_name is a string"""
        self.assertEqual(str, type(User.first_name))

    def test_str_last_name(self):
        """Check if last_name is a string"""
        self.assertEqual(str, type(User.last_name))


if __name__ == '__main__':
    unittest.main()
