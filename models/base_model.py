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
    def __init__(self, *args, **kwargs):
        """The base class constructer"""
        if kwargs != {}:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, date_format)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
    
    def save(self):
        """A public instance method that updates "updated_at" attribute"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """A public instance method that returns a dictionary"""
        dictionary_rep = self.__dict__.copy()
        dictionary_rep['__class__'] = self.__class__.__name__
        dictionary_rep['created_at'] = self.created_at.isoformat()
        dictionary_rep['updated_at'] = self.updated_at.isoformat()
        return dictionary_rep
    
    def __str__(self):
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

#obj = BaseModel()
#my_obj_dict = obj.to_dict()
#print(my_obj_dict)
#print(obj.id)
#print(obj.created_at)
#print(obj.updated_at)
#print(str(obj))
if __name__ == "__main__":
    BaseModel()
