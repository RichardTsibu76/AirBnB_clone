#!/usr/bin/python3
"""A class that creates a user"""
from models.base_model import BaseModel
import json


class User(BaseModel):
    """subclass of the BaseModel class
    Attributes:
         email (str) -> User's email
         password (str) -> User's password
         first_name (str) -> User's first Name
         last_name (str) -> User's last Name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
