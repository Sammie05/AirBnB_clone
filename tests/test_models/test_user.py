#!/usr/bin/python3


"""
This module contains all the test cases for the user class attributes
"""

import unittest
from models.base_model import BaseModel
from models.user import user


class Testuserclass(unittest.TestCase):
    """Test cases for the user class in the models/user module"""

    def setUp(self):
        """sets up test methods,(makes sure tests are executed)"""
        pass

    def tearDown(self):
        """Tears down test methods for execution"""
        pass

    def test_if_class_attributes_exit(self):
        """verify user class has 'first_name' and last_ name' attributes"""
        user = User()
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertTrue(hasattr(User, 'last_name'))

    def test_class_attributes_type_and_initials(self):
        """
        Verify 'first_name' and 'last_name' have correct
        data types and initial values.
        """

        user = User()
        self.assertIs(type(user.first_name), str)
        self.assertIs(type(user.last_name),str)
        self.assertFalse(bool(user.first_name))
        self.assertFalse(bool(user.last_name))
        self.assertTrue(user.first_name == "")
        self.assertTrue(user.last_name == "")

    def test_user_class_is_BaseModel_subclass(self):
        """
        Verify User class is a subclass of BaseModel.
        """
        user = User()
        self.assertTrue(issubclass(type(user), BaseModel))
