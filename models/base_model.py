#!/usr/bin/python3
"""Module whit class BaseModel"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """class that defines all common
    attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Inizialite BaseModel"""

        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
            del kwargs["__class__"]
            self.__dict__.update(kwargs)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            
    def to_dict(self):
        """Dictionary from save class"""
        BaseDict = self.__dict__.copy()
        BaseDict["__class__"] = self.__class__.__name__
        BaseDict["created_at"] = self.created_at.isoformat()
        BaseDict["updated_at"] = self.updated_at.isoformat()
        return (BaseDict)

    def __str__(self):
        """Containing all keys/values of __dict__ of the instance"""
        classname = self.__class__.__name__
        return (f"[{classname}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates the public instance attribute
        updated_atwith the current datetime"""
        self.updated_at = datetime.now()
