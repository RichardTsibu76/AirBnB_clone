#!/usr/bin/python3
""" A model that defines the BaseModel class"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """ A class  that defines all attributes/methods for other classes.

    Attributes:
        id: Public instance attributes that assignes Id
        created_at: assign current datetime when an instance is created
        updated_at: update current datetime when an instance is updated
    """

    def __init__(self, *args, **kwargs):
        """The base class constructer"""
        if kwargs:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    if isinstance(value, str):
                        value = datetime.strptime(value, date_format)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        if not hasattr(self, "id"):
            self.id = str(uuid.uuid4())

    def save(self):
        """A public instance method that updates "updated_at" attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """A public instance method that returns a dictionary"""
        dictionary_rep = self.__dict__.copy()
        dictionary_rep['__class__'] = self.__class__.__name__
        dictionary_rep['created_at'] = self.created_at.isoformat()
        dictionary_rep['updated_at'] = self.updated_at.isoformat()
        return dictionary_rep

    def __str__(self):
        """"A public instance method that returns the str rep of the
        class name with id.
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"


if __name__ == "__main__":
    BaseModel()
