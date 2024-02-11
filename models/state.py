#!/usr/bin/python3
"""A class that creates a user"""
from models.base_model import BaseModel


class State(BaseModel):
    """subclass of the BaseModel class
    Attributes:
         "name": state name
    """
    
    name = " "
