#!/usr/bin/python3
""" A model that defined the BaseModel class"""
import uuid
import json
from datetime import datetime


class BaseModel():
    """ A class  that defines all attributes/methods for other classes.

    Attributes:
        id:
        created_at:
        updated_at:
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def save(self):
        """A public instance method that updates "updated_at" attribute"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """A public instance method that returns a dictionary"""
        class_name = self.__class__.__name__
        dictionary_rep = {
                "__class__": class_name,
                "id": self.id,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat()
        }
        return dictionary_rep
    
    def __str__(self):
        class_name = self.__class__.__name__
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

#obj = BaseModel()
#print(obj.id)
#print(obj.created_at)
#print(obj.updated_at)
#print(str(obj))
if __name__ == "__main__":
    BaseModel()
