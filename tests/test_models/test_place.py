#!/usr/bin/python3
"""Unittest for User"""

import unittest
from models.place import Place


class testPlace(unittest.TestCase):
    """Test for Place Class"""
    def test_str_city_id(self):
        """Check if city_id is a string"""
        self.assertEqual(str, type(Place.city_id))

    def test_str_user_id(self):
        """Check if user_id is a string"""
        self.assertEqual(str, type(Place.user_id))

    def test_str_name(self):
        """Check if name is a string"""
        self.assertEqual(str, type(Place.name))

    def test_str_description(self):
        """Check if description is a string"""
        self.assertEqual(str, type(Place.description))

    def test_int_number_rooms(self):
        """Check if number_rooms is a integer"""
        self.assertEqual(int, type(Place.number_rooms))

    def test_int_number_bathrooms(self):
        """Check if number_bathrooms is a integer"""
        self.assertEqual(int, type(Place.number_bathrooms))

    def test_int_max_guest(self):
        """Check if max_guest is a integer"""
        self.assertEqual(int, type(Place.max_guest))

    def test_int_price_by_night(self):
        """Check if price_by_night is a integer"""
        self.assertEqual(int, type(Place.price_by_night))

    def test_float_latitude(self):
        """Check if latitude is a float"""
        self.assertEqual(float, type(Place.latitude))

    def test_float_longitude(self):
        """Check if longitude is a float"""
        self.assertEqual(float, type(Place.longitude))

    def test_list_amenity_ids(self):
        """Check if amenity_ids is a list of string"""
        self.assertEqual(list, type(Place.amenity_ids))


if __name__ == '__main__':
    unittest.main()
