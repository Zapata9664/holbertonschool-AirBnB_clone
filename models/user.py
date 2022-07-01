#!/usr/bin/python3
"""Module for Class User from BaseModel"""
from models.base_model import BaseModel

class User(BaseModel):
    """"Class User that inherits from BaseMode"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
