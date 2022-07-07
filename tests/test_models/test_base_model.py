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

    def test_instance_updatedat(self):
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

    def test_dic(self):
        """Check if dic is a dictionary"""
        dic = BaseModel().to_dict()
        self.assertIsInstance(dic, dict)

    def test_base_instance(self):
        """Check if instace is a Intance of BaseModel"""
        self.assertIsInstance(BaseModel(), BaseModel)

    def test_id(self):
        """Check if id in an instance"""
        self.assertTrue(hasattr(BaseModel(), "id"), True)


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


class testBaseModel_dic(unittest.TestCase):
    """Tests for public instance methods: dic"""

    def test_correct_data(self):
        """Check de correct data"""
        instance = BaseModel()
        self.assertIn("id", instance.to_dict())
        self.assertIn("created_at", instance.to_dict())
        self.assertIn("updated_at", instance.to_dict())
        self.assertIn("__class__", instance.to_dict())

    def test_add_attributes(self):
        """Check if add correct attributes"""
        instance = BaseModel()
        instance.price_by_night = "7.500"
        instance.state_id = "Bello"
        self.assertIn = ("price_by_night", instance.to_dict())
        self.assertIn = ("state_id", instance.to_dict())

    def test_output(self):
        """Compare output with a dictionary"""
        time = datetime.now()
        instance = BaseModel()
        instance.id = "0d11af78-4e5e-4a80-ac9b-faaaf8eb2432"
        instance.created_at = instance.updated_at = time
        dic = {
            "id": "0d11af78-4e5e-4a80-ac9b-faaaf8eb2432",
            "created_at": time.isoformat(),
            "updated_at": time.isoformat(),
            "__class__": "BaseModel"
        }
        self.assertDictEqual(instance.to_dict(), dic)

    def test_whit_arg(self):
        """Check dict None"""
        instance = BaseModel()
        with self.assertRaises(TypeError):
            instance.to_dict(None)

    def test_to_dict_values(self):
        """Tests correct format"""
        instance = BaseModel()
        dic = instance.to_dict()
        self.assertEqual(dic["__class__"], "BaseModel")
        self.assertEqual(type(dic["created_at"]), str)
        self.assertEqual(type(dic["updated_at"]), str)
        self.assertEqual(dic["created_at"],
                         instance.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(dic["updated_at"],
                         instance.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))


class TestBaseModel_str(unittest.TestCase):
    """Tests for public instance methods: dic"""

    def test_str(self):
        string1 = BaseModel().__str__()
        self.assertEqual(str, type(string1))

    def test__str__(self):
        """Check if __str__ is a method"""
        self.assertTrue(hasattr(BaseModel, "__str__"), True)


if __name__ == '__main__':
    unittest.main()
