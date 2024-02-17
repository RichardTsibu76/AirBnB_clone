import time
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):

    def test_default_values(self):
        """
        Test that the default values of Place attributes are as expected.
        """
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_setting_values(self):
        """
        Test setting the attributes of Place.
        """
        place = Place()
        place.city_id = "1"
        place.user_id = "2"
        place.name = "Luxury Villa"
        place.description = "A stunning villa with breathtaking views"
        place.number_bathrooms = 3
        place.number_rooms = 4
        place.max_guest = 8
        place.price_by_night = 500
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = [1, 2, 3]

        self.assertEqual(place.city_id, "1")
        self.assertEqual(place.user_id, "2")
        self.assertEqual(place.name, "Luxury Villa")
        self.assertEqual(place.description, "A stunning villa with breathtaking views")
        self.assertEqual(place.number_bathrooms, 3)
        self.assertEqual(place.number_rooms, 4)
        self.assertEqual(place.max_guest, 8)
        self.assertEqual(place.price_by_night, 500)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, [1, 2, 3])

    def test_inheritance(self):
        """
        Test that Place inherits from BaseModel.
        """
        place = Place()
        self.assertTrue(isinstance(place, BaseModel))

if __name__ == '__main__':
    unittest.main()

