#!/usr/bin/python3
"""Unittest for BaseModel"""

import unittest
from models.base_model import BaseModel


class testBaseModel(unittest.TestCase):
    """Test for BaseModel Class"""
    def test_same_string(self):
        """Check if id is a string"""
        self.assertNotEqual(str, BaseModel().id)

    def test_instance_id(self):
        """Check if id is a intance of BaseModel"""
        self.assertTrue(hasattr(BaseModel(), "id"), True)

    def test_instance_createdat(self):
        """Check if created_at is a intance of BaseModel"""
        self.assertTrue(hasattr(BaseModel(), "created_at"), True)

    def test_instance(self):
        """Check if updated_at is a intance of BaseModel"""
        self.assertTrue(hasattr(BaseModel(), "updated_at"), True)


if __name__ == '__main__':
    unittest.main()
