#!/usr/bin/python3
"""Module for unittest init"""

import unittest
from models.__init__ import storage


class test__init__(unittest.TestCase):
    """class for test of init"""

    def test_variable(self):
        """Check if storage exist"""
        self.assertTrue(storage, True)


if __name__ == "__main__":
    unittest.main()
