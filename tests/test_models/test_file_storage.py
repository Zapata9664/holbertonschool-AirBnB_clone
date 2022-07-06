#!/usr/bin/python3
"""Module for unittest file_storage"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class test_file_storage(unittest.TestCase):
    """Test for file file_storage"""
    def test_object(self):
        """Check instance"""
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_file_path(self):
        """Check untance attribute of BaseModel"""
        self.assertFalse(hasattr(FileStorage(), "__file_path"), False)

    def test_method_new(self):
        """Check if new is a method of file_instance"""
        self.assertTrue(hasattr(FileStorage(), "new"), True)

    def test_method_save(self):
        """Check if save is a method of file_inst"""
        self.assertTrue(hasattr(FileStorage(), "save"), True)

    def test_method_all(self):
        """Check if all is a method of file_inst"""
        self.assertTrue(hasattr(FileStorage(), "all"), True)

    def test_method_reload(self):
        """Check if reload is a method of file_inst"""
        self.assertTrue(hasattr(FileStorage(), "reload"), True)

    def test_for_reload(self):
        """Check if reload is a method of file_inst"""
        self.assertTrue(hasattr(FileStorage(), "reload"), True)

    def test_all_returns_dict(self):
        """check if all return FileStorage.__objects attr"""
        dic = FileStorage().all()
        self.assertEqual(type(dic), dict)
        self.assertIs(dic, FileStorage()._FileStorage__objects)


if __name__ == "__main__":
    unittest.main()
