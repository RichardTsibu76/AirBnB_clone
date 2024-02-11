import time
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):

    def test_default_name(self):
        """
        Test that the default name of Amenity is an empty string.
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_setting_name(self):
        """
        Test setting the name of Amenity.
        """
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_inheritance(self):
        """
        Test that Amenity inherits from BaseModel.
        """
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, BaseModel))

if __name__ == '__main__':
    unittest.main()

