#!/usr/bin/python3
"""Module with class FileStorage"""
from models.base_model import BaseModel
import json


class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj
        with key <obj class name>.id"""
        FileStorage.__objects["{}.{}".format(
            obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """"""

        with open(FileStorage.__file_path, "w") as file:
            json.dump(FileStorage.__objects, file)