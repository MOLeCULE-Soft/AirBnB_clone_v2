#!/usr/bin/python3
"""Console Test Module"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    """Console test class implementation"""

    def setUp(self):
        self.console_stdout = StringIO()

    def tearDown(self):
        self.console_stdout.close()

    def test_help_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("help show")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "Shows the string representation of an instance")

    def test_class_check_exists(self):
        """Test class_check with existing class."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.class_check("User")
            output = f.getvalue()
            print(output)
        self.assertEqual(output, True)

    def test_class_check_nonexistent(self):
        """Test class_check with nonexistent class."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.class_check("NonexistentClass")
            output = f.getvalue()
        self.assertEqual(output, "** class doesn't exist **\n")

    def test_class_check_missing_arg(self):
        """Test class_check with missing argument."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.class_check()
            output = f.getvalue()
        self.assertEqual(output, "** class name missing **\n")

    def test_do_create_valid(self):
        """Test do_create with valid arguments."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_create("User")
            output = f.getvalue()
            self.assertTrue("[A-Za-z0-9]{32}" in output)

    def test_do_create_invalid(self):
        """Test do_create with invalid arguments."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_create("NonexistentClass")
            output = f.getvalue()
        self.assertEqual(output, "** class doesn't exist **\n")

    def test_do_show_valid(self):
        """Test do_show with valid arguments."""
        # Create a user first
        user = User(email="test@example.com", password="1234")
        user.save()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_show("User", user.id)
            output = f.getvalue()
        self.assertIn(str(user), output)

    def test_do_show_invalid_class(self):
        """Test do_show with invalid class."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_show("NonexistentClass", "invalid_id")
            output = f.getvalue()
        self.assertEqual(output, "** class doesn't exist **\n")

    def test_do_show_missing_id(self):
        """Test do_show with missing id."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_show("User", "")
            output = f.getvalue()
        self.assertEqual(output, "** instance id missing **\n")

    def test_do_destroy_valid(self):
        """Test do_destroy with valid arguments."""
        # Create a user first
        user = User(email="test@example.com", password="1234")
        user.save()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_destroy("User", user.id)
            output = f.getvalue()
        self.assertIn(user.id, output)

    def test_do_destroy_invalid_class(self):
        """Test do_destroy with invalid class."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_destroy("NonexistentClass", "invalid_id")
            output = f.getvalue()
        self.assertEqual(output, "** class doesn't exist **\n")

    def test_do_destroy_missing_id(self):
        """Test do_destroy with missing id."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_destroy("User", "")
            output = f.getvalue()
        self.assertEqual(output, "** instance id missing **\n")

if __name__ == '__main__':
    unittest.main()
