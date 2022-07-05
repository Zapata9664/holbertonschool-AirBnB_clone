#!/usr/bin/python3
"""Unittest for User"""

import unittest
from models.state import State


class testState(unittest.TestCase):
    """Test for State Class"""
    def test_str_name(self):
        """Check if name is a string"""
        self.assertEqual(str, type(State.name))


if __name__ == '__main__':
    unittest.main()
