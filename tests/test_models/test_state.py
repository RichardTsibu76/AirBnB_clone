import time
import unittest
from models.state import State

class TestState(unittest.TestCase):

    def test_default_values(self):
        """
        Test that the default value of the name attribute is an empty string.
        """
        state = State()
        self.assertEqual(state.name, "")

    def test_setting_name(self):
        """
        Test setting the name attribute.
        """
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_inheritance(self):
        """
        Test that State inherits from BaseModel.
        """
        state = State()
        self.assertIsInstance(state, BaseModel)

if __name__ == '__main__':
    unittest.main()

