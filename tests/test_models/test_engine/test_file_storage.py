#!/usr/bin/python3
"""Module for unittest file_storage"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.amenity import Amenity


class test_file_storage(unittest.TestCase):
    """Test for file file_storage"""
    def test_object(self):
        """Check instance"""
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_file_path(self):
        """Check untance attribute of BaseModel"""
        self.assertFalse(hasattr(FileStorage(), "__file_path"), False)

    def test_method_new(self):
        """Check if new is a method of file_inst"""
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

    def test_private_str(self):
        """Check private string"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_private_dic(self):
        """Check private dic"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_initializes(self):
        """initialize storage"""
        self.assertEqual(type(storage), FileStorage)


class TestFileStorage_met(unittest.TestCase):
    """Class for test methods"""

    def test_for_same_type(self):
        """Testing that storage same type of dict"""
        self.assertEqual(dict, type(storage.all()))

    def test_all_arg(self):
        """Testing all args arg"""
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new_args(self):
        """Testing new arguments"""
        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 1)

    def test_reload_args(self):
        """Chesk reaload with arguments"""
        with self.assertRaises(TypeError):
            storage.reload(None)

    def test_save(self):
        """Check for method save"""
        storage.new(BaseModel())
        storage.new(User())
        storage.new(Place())
        storage.new(Amenity())
        storage.save()
        storage.reload()
        endic = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + BaseModel().id, endic)
        self.assertIn("User." + User().id, endic)
        self.assertIn("Place." + Place().id, endic)
        self.assertIn("Amenity." + Amenity().id, endic)


if __name__ == "__main__":
    unittest.main()
