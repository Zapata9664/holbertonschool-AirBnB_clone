#!/usr/bin/python3
"""Module with class FileStorage"""
from models.base_model import BaseModel
from models.user import User
import json

classtype = {
    "BaseModel": BaseModel,
    "User": User,

}

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
        """serializes __objects to the JSON file"""
        dict = {}
        for key, value in self.__objects.items():
            dict.update({key: value.to_dict()})
        with open(FileStorage.__file_path, "w") as file:
            json.dump(dict, file)

    def reload(self):
        """deserializes the JSON file to __objects only if
        the JSON file exists; otherwise, do nothing"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    search = classtype[value["__class__"]](**value)
                    dict = {key: search}
                    self.__objects.update(dict)
        except Exception:
            pass
