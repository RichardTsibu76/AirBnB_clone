#!/usr/bin/python
''' Define class Review that inherits from BaseModel '''
from models.base_model import BaseModel


class Review(BaseModel):
    """ Representation of Review """

    place_id = ""
    user_id = ""
    text = ""
