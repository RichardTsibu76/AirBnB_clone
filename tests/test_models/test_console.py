import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_create_command_missing_class(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create"))
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_create_command_invalid_class(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create SomeInvalidClass"))
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_create_command_valid_class(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("create BaseModel"))
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) > 0)

if __name__ == '__main__':
    unittest.main()

