#!/usr/bin/python3
"""A class that creates a user"""
from models.base_model import BaseModel
import json


class User(BaseModel):
    """subclass of the BaseModel class"""
    
    email = " "
    password = " "
    first_name = " "
    last_name = " "
