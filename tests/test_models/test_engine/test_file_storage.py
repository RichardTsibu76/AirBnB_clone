#!/usr/bin/python3
import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = "test_file.json"
        self.file_storage = FileStorage()
        self.obj1 = BaseModel()
        self.obj2 = User()
        self.obj3 = State()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        # Test if all() returns a dictionary
        self.assertIsInstance(self.file_storage.all(), dict)

    def test_new(self):
        # Test if new() adds an object to the dictionary
        self.file_storage.new(self.obj1)
        self.assertIn("BaseModel.{}".format(self.obj1.id), self.file_storage.all())

    def test_save_reload(self):
        # Test if save() and reload() work together
        self.file_storage.new(self.obj2)
        self.file_storage.save()
        new_file_storage = FileStorage()
        new_file_storage.reload()
        self.assertIn("User.{}".format(self.obj2.id), new_file_storage.all())

    def test_save_file_exists(self):
        # Test if save() creates a file
        self.file_storage.save()
        self.assertTrue(os.path.exists(self.file_storage._FileStorage__file_path))

    def test_reload_instantiate_objects(self):
        # Test if reload() instantiates correct objects
        self.file_storage.new(self.obj3)
        self.file_storage.save()
        new_file_storage = FileStorage()
        new_file_storage.reload()
        obj_key = "State.{}".format(self.obj3.id)
        self.assertIsInstance(new_file_storage.all()[obj_key], State)

    def test_set_up_teardown(self):
        """Test if set up and teardown methods work correctly"""
        self.assertIsInstance(self.file_storage, FileStorage)
        self.assertIsInstance(self.obj1, BaseModel)
    
    def test_file_exists_after_set_up(self):
        """Test if file.json exists after setup"""
        self.assertTrue(os.path.isfile("file.json"))

    def test_rename_tempfile_back_after_teardown(self):
        """Test if 'tempfile' is renamed back to 'file.json' after teardown"""
        self.assertFalse(os.path.isfile("tempfile"))
        self.assertTrue(os.path.isfile("file.json"))

    def test_attributes_after_set_up(self):
        """Test the attributes after setup"""
        self.assertTrue(hasattr(self.obj1, "created_at"))
        self.assertTrue(hasattr(self.obj1, "updated_at"))
        self.assertTrue(hasattr(self.obj1, "id"))
        self.assertTrue(hasattr(self.obj1, "__class__"))
        self.assertEqual(self.obj1.__class__.__name__, "BaseModel")
        self.assertEqual(self.file_storage._FileStorage__file_path, "file.json")
        self.assertTrue(isinstance(self.file_storage._FileStorage__objects, dict))

    def test_all_method_after_save(self):
        """Test the all method after calling save"""
        new_obj = BaseModel()
        self.file_storage.new(new_obj)
        self.file_storage.save()
        all_objs_dict = self.file_storage.all()
        new_obj_id = "BaseModel." + new_obj.id
        self.assertIn(new_obj_id, all_objs_dict)

    def test_reload_method_after_save(self):
        """Test the reload method after calling save"""
        self.file_storage.save()
        temp_base = BaseModel()
        temp_base.save()
        temp_base_id = "BaseModel." + temp_base.id
        self.file_storage.reload()
        self.assertIn(temp_base_id, self.file_storage.all())
        del temp_base

if __name__ == '__main__':
    unittest.main()

