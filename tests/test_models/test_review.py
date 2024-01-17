#!/usr/bin/python3



"""
This module contain all the test cases for the review class attributes
"""


import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReviewClass(unittest.Testcase):
    """Test cases against the review class in the models/review module"""

    def setUp(self):
        self.review = Review()

    def test_Review_is_BaseModule_subclass(self):
        """
        verify Review class is a subclass of BaseModel
        """
        self.assertTrue(issubclass(type(self.review), BaseModel))

    def test_if_class_attributes_exit(self):
        """verify Reviews class has place_id and text attributes"""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))

    def test_class_attributes_type_and_initials(self):
        """
        Verify 'place_id' and 'user_id' attributes have correct
        data types and initial values.
        """
        
        self.assertIs(type(self.review.place_id), str)
        self.assertTrue(self.review.place_id == "")
        self.assertIs(type(self.review.user_id), str)
        self.assertTrue(self.review.user_id == "")
        self.assertFalse(bool(getattr(self.review, 'place_id')))
        self.assertFalse(bool(getattr(self.review, 'user_id')))#!/usr/bin/python3



        """
        This module contain all the test cases for the review class attributes
        """


        import unittest
        from models.base_model import BaseModel
        from models.review import Review


        class TestReviewClass(unittest.Testcase):
            """Test cases against the review class in the models/review module"""

            def setUp(self):
                self.review = Review()

            def test_Review_is_BaseModule_subclass(self):
                """
                verify Review class is a subclass of BaseModel
                """
                self.assertTrue(issubclass(type(self.review), BaseModel))

            def test_if_class_attributes_exit(self):
                """verify Reviews class has place_id and text attributes"""
                self.assertTrue(hasattr(self.review, 'place_id'))
                self.assertTrue(hasattr(self.review, 'user_id'))

            def test_class_attributes_type_and_initials(self):
                """
                Verify 'place_id' and 'user_id' attributes have correct
                data types and initial values.
                """
                
                self.assertIs(type(self.review.place_id), str)
                self.assertTrue(self.review.place_id == "")
                self.assertIs(type(self.review.user_id), str)
                self.assertTrue(self.review.user_id == "")
                self.assertFalse(bool(getattr(self.review, 'place_id')))
                self.assertFalse(bool(getattr(self.review, 'user_id')))
