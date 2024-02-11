import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def test_default_values(self):
        """
        Test that the default values of state_id and name of City are empty strings.
        """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_setting_values(self):
        """
        Test setting the state_id and name of City.
        """
        city = City()
        city.state_id = "CA"
        city.name = "San Francisco"
        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "San Francisco")

    def test_inheritance(self):
        """
        Test that City inherits from BaseModel.
        """
        city = City()
        self.assertTrue(isinstance(city, BaseModel))

if __name__ == '__main__':
    unittest.main()

