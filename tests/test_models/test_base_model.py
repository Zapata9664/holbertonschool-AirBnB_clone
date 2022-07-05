#!/usr/bin/python3
"""Unittest for BaseModel"""

import unittest
from models.base_model import BaseModel


class testBaseModel(unittest.TestCase):
    """Test for BaseModel Class"""
    def test_same_string(self):
        """Check if id is a string"""
        self.assertNotEqual(str, BaseModel().id)
