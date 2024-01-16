#!/usr/bin/python3
"""Contains unittest for User.py"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_attributes_initialization(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_setting_attributes(self):
        user = User()
        user.email = ""
        user.password = ""
        user.first_name = ""
        user.last_name = ""
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

if __name__ == '__main__':
    unittest.main()
