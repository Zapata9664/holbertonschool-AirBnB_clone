#!/usr/bin/python3
"""Module with class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """class City that inherit from BaseModel"""
    name = ""
    state_id = ""  # it will be the State.id
