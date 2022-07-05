#!/usr/bin/python3
"""Unittest for BaseModel"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


class testBaseModel(unittest.TestCase):
    """Test for BaseModel Class"""

    def test_equal_string(self):
        """Check if id is a string"""
        self.assertEqual(str, type(BaseModel().id))

    def test_unique_id(self):
        """Check if the id in unique"""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_instance_id(self):
        """Check if id is a intance of BaseModel"""
        self.assertTrue(hasattr(BaseModel(), "id"), True)

    def test_instance_createdat(self):
        """Check if created_at is a intance of BaseModel"""
        self.assertTrue(hasattr(BaseModel(), "created_at"), True)

    def test_instance(self):
        """Check if updated_at is a intance of BaseModel"""
        self.assertTrue(hasattr(BaseModel(), "updated_at"), True)

    def test_public_datetime(self):
        """Test for a make public datetime"""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_public_datetime_updated(self):
        """Test for a make public datetime"""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_less_time_createdat(self):
        """Check less time in created_at"""
        instance1 = BaseModel()
        sleep(0.2)
        instance2 = BaseModel()
        self.assertLess(instance1.created_at, instance2.created_at)

    def test_less_time_updatedat(self):
        """Check less time in updated_at"""
        instance1 = BaseModel()
        sleep(0.2)
        instance2 = BaseModel()
        self.assertLess(instance1.updated_at, instance2.updated_at)


class TestBaseModel_save(unittest.TestCase):
    """Tests for public instance methods: Save"""

    def test_save_one_instance(self):
        """Save one instance"""
        instance1 = BaseModel()
        sleep(0.2)
        updated1 = instance1.updated_at
        instance1.save()
        self.assertLess(updated1, instance1.updated_at)

    def test_save_tow_instances(self):
        """Save two instances"""
        instance1 = BaseModel()
        sleep(0.2)
        updated1 = instance1.updated_at
        instance1.save()
        updated2 = instance1.updated_at
        self.assertLess(updated1, updated2)
        sleep(0.2)
        instance1.save()
        self.assertLess(updated2, instance1.updated_at)

    def test_save_updates(self):
        """Save updates in dictionary"""
        instance = BaseModel()
        instance.save()
        instanceId = "BaseModel" + "." + instance.id
        with open("file.json", "r") as f:
            self.assertIn(instanceId, f.read())


if __name__ == '__main__':
    unittest.main()
