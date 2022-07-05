#!/usr/bin/python3
"""Unittest for User"""

import unittest
from models.review import Review


class testState(unittest.TestCase):
    """Test for State Class"""
    def test_str_place_id(self):
        """Check if place_id is a string"""
        self.assertEqual(str, type(Review.place_id))

    def test_str_user_id(self):
        """Check if user_id is a string"""
        self.assertEqual(str, type(Review.user_id))

    def test_str_text(self):
        """Check if text is a string"""
        self.assertEqual(str, type(Review.text))


if __name__ == '__main__':
    unittest.main()
