#!/usr/bin/python3
"""Contains tests for city.py"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Class for tests on City class"""

    def setUp(self):
        self.city = City()

    def test_attributes(self):
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_instance(self):
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)

if __name__ == '__main__':
    unittest.main()
