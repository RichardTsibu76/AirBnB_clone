import time
import unittest
from models.user import User

class TestUser(unittest.TestCase):

    def test_default_values(self):
        """
        Test that the default values of User attributes are as expected.
        """
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_setting_values(self):
        """
        Test setting the attributes of User.
        """
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_inheritance(self):
        """
        Test that User inherits from BaseModel.
        """
        user = User()
        self.assertIsInstance(user, BaseModel)

if __name__ == '__main__':
    unittest.main()

