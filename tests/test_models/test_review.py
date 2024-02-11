import unittest
from models.review import Review

class TestReview(unittest.TestCase):

    def test_default_values(self):
        """
        Test that the default values of Review attributes are as expected.
        """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_setting_values(self):
        """
        Test setting the attributes of Review.
        """
        review = Review()
        review.place_id = "1"
        review.user_id = "2"
        review.text = "This place was amazing!"

        self.assertEqual(review.place_id, "1")
        self.assertEqual(review.user_id, "2")
        self.assertEqual(review.text, "This place was amazing!")

    def test_inheritance(self):
        """
        Test that Review inherits from BaseModel.
        """
        review = Review()
        self.assertTrue(isinstance(review, BaseModel))

if __name__ == '__main__':
    unittest.main()

