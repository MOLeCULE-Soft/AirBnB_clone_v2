#!/usr/bin/python3
"""Contains tests for review.py"""

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Unit tests for the Review class"""

    def test_review_attributes(self):
        review = Review(place_id="", user_id="", text="")
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

if __name__ == '__main__':
    unittest.main()
