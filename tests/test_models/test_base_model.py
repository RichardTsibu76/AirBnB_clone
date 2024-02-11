import time
import unittest
from datetime import datetime, timedelta
from models.base_model import BaseModel
import uuid


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_attributes_existence(self):
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(original_updated_at, self.base_model.updated_at)

    def test_to_dict_returns_dict(self):
        result = self.base_model.to_dict()
        self.assertIsInstance(result, dict)

    def test_to_dict_contains_expected_keys(self):
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        result = self.base_model.to_dict()
        self.assertTrue(all(key in result for key in expected_keys))

    def test_to_dict_created_at_format(self):
        result = self.base_model.to_dict()
        self.assertEqual(result['created_at'], self.base_model.created_at.isoformat())

    def test_to_dict_updated_at_format(self):
        result = self.base_model.to_dict()
        self.assertEqual(result['updated_at'], self.base_model.updated_at.isoformat())

    def test_str_representation(self):
        expected_str = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)

    def test_str_representation_with_custom_attributes(self):
        custom_model = BaseModel(custom_attr='test')
        expected_str = f"[BaseModel] ({custom_model.id}) {custom_model.__dict__}"
        self.assertEqual(str(custom_model), expected_str)

    def test_kwargs_constructor(self):
        new_model = BaseModel(id='123', created_at=datetime.now(), updated_at=datetime.now())
        self.assertEqual(new_model.id, '123')
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)

    def test_created_at_and_updated_at_for_existing_instance_after_delayed_save(self):
        existing_model = BaseModel()
        original_updated_at = existing_model.updated_at
        existing_model.save()
        new_updated_at = existing_model.updated_at
        self.assertGreater(new_updated_at, original_updated_at)

    def test_to_dict_and_str_after_delayed_save(self):
        delayed_save_model = BaseModel()
        original_dict = delayed_save_model.to_dict()
        delayed_save_model.save()
        new_dict = delayed_save_model.to_dict()
        self.assertNotEqual(original_dict, new_dict)

    def test_to_dict_and_str_after_multiple_saves(self):
        multiple_saves_model = BaseModel()
        original_dict = multiple_saves_model.to_dict()
        multiple_saves_model.save()
        multiple_saves_model.save()
        new_dict = multiple_saves_model.to_dict()
        self.assertNotEqual(original_dict, new_dict)


if __name__ == '__main__':
    unittest.main()

