#!/usr/bin/python3

import models
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def test_attributes(self):
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_generation(self):
        # Check if IDs are generated and unique
        another_base_model = BaseModel()
        self.assertNotEqual(self.base_model.id, another_base_model.id)

    def test_save_method(self):
        # Check if save method updates 'updated_at'
        prev_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(prev_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        # Check if to_dict method returns a dictionary with expected keys and values
        expected_dict = {
            '__class__': 'BaseModel',
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat()
        }
        self.assertDictEqual(self.base_model.to_dict(), expected_dict)

    def test_initialization_with_kwargs(self):
        # Check if initialization with kwargs works as expected
        new_base_model = BaseModel(id=self.base_model.id,
                                   created_at=self.base_model.created_at.isoformat(),
                                   updated_at=self.base_model.updated_at.isoformat())
        self.assertEqual(self.base_model.id, new_base_model.id)
        self.assertEqual(self.base_model.created_at, new_base_model.created_at)
        self.assertEqual(self.base_model.updated_at, new_base_model.updated_at)

    def test_string_representation(self):
        # Check if string representation contains class name and id
        string_repr = str(self.base_model)
        self.assertIn('BaseModel', string_repr)
        self.assertIn(self.base_model.id, string_repr)

if __name__ == '__main__':
    unittest.main()
