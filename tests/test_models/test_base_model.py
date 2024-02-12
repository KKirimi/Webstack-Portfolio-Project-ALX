#!/usr/bin/python3
import unittest
import uuid
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class"""


def test_init(self):
    """Test initialization of BaseModel instance"""
    model = BaseModel()
    self.assertIsInstance(model, BaseModel)
    self.assertIsInstance(model.id, str)
    self.assertIsInstance(model.created_at, datetime)
    self.assertIsInstance(model.updated_at, datetime)


def test_str(self):
    """Test __str__ method"""
    model = BaseModel()
    expected_str = f"[BaseModel]({model.id}) {
        {'id': '{model.id}', 'created_at': '{
            model.created_at}', 'updated_at': '{model.updated_at}'}}"
    self.assertEqual(str(model), expected_str)


def test_save(self):
    """Test save method"""
    model = BaseModel()
    initial_updated_at = model.updated_at
    model.save()
    self.assertNotEqual(initial_updated_at, model.updated_at)


def test_to_dict(self):
    """Test to_dict method"""
    model = BaseModel()
    model_dict = model.to_dict()
    self.assertIsInstance(model_dict, dict)
    self.assertIn('__class__', model_dict)
    self.assertEqual(model_dict['__class__'], 'BaseModel')
    self.assertIn('id', model_dict)
    self.assertEqual(model_dict['id'], model.id)
    self.assertIn('created_at', model_dict)
    self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
    self.assertIn('updated_at', model_dict)
    self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
