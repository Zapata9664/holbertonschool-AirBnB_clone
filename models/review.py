#!/usr/bin/python3
"""Module with class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review that inherit from BaseModel"""
    place_id = ""  # it will be the Place.id
    user_id = ""  # it will be the User.id
    text = ""
