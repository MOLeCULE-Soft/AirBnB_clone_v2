#!/usr/bin/python3
"""Contains tests for state.py"""

import unittest
from models.state import State

class TestState(unittest.TestCase):
    """State class implementation"""

    def test_state_name(self):
        state = State()
        state.name = ""
        self.assertEqual(state.name, "")

if __name__ == '__main__':
    unittest.main()
