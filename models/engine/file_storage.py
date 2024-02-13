#!/usr/bin/python3
"""Defines the FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """ the FileStorage class of the AirBnB Clone Project"""
    __file_path = "file.json"
    __objects = {}
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review":  Review,
    }

    def __init__(self):
        """initiates file_storage class"""
        pass

    def all(self):
        """Returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """A Public instance method that sets in the dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes objects to JSON file"""
        serialized_dict = {}
        for key, obj in FileStorage.__objects.items():
            serialized_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_dict, file)

    def reload(self):
        """Deserializes the JSON file to objects"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for key, obj in data.items():
                    class_name, obj_id = key.split(".")
                    objt = FileStorage.class_dict[obj["__class__"]](**obj)
                    FileStorage.__objects[key] = objt
        except FileNotFoundError:
            pass
