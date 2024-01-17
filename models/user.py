#!/usr/bin/python3
""" This module contains the User class (Child-class to BaseModel) """
from models.base_model import BaseModel


class User(BaseModel):
    """
    Implement the user class.

    Args:
        email(str): the user's emial.
        password(str): the user's password.
        first_name(str): the user's first nsme.
        last_name(str): the user's last name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = """
