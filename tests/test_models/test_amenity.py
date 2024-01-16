#!/usr/bin/python3
"""Contains tests for amenity.py"""

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Tests for the Amenity class"""

    def test_default_name(self):
        """Test if the default name is an empty string"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_setting_name(self):
        """Test setting the name attribute"""
        amenity = Amenity()
        amenity.name = ""
        self.assertEqual(amenity.name, "")

if __name__ == '__main__':
    unittest.main()
