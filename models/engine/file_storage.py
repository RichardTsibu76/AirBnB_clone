#!/usr/bin/python3
"""Defines the FileStorage class"""
import json
from models.base_model import BaseModel

class FileStorage():
    """ """
    def __init__(self):
        """initiates file_storage class
            
       Attributes:
       __filepath:
       __objects: 
       """
        self.__file_path = "file.json"#string - path to the JSON file (ex: file.json)
        self.__objects = {} #dictionary - empty but will store all objects by <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)

    def all(self):
        """Returns the dictionary"""
        return self.__objects
    def new(self, obj):
        """A Public instance method that sets in the dictionary"""
        #sets in __objects the obj with key <obj class name>.id
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
    def save(self):
        """serializes objects to JSON file"""
        #serializes __objects to the JSON file (path: __file_path)
        serialized_dict = {}
        for key, obj in self.__objects.items():
            serialized_dict[key] = obj.to_dict()
        with open(self.__file_path, "w", encoding ="utf-8") as file:
            json.dump(serialized_dict, file)
    def reload(self): 
        """Deserializes the JSON file to objects"""
        #if the JSON file (__file_path) exist#if the JSON file (__file_path) exist
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    obj = globals()[class_name](**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            #otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
            pass
