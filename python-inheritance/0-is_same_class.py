"""
Module 0-square
This module defines a a function that returns True if the object is exactly an instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Parameters:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is exactly an instance of the specified class; otherwise, False.
    """
    return type(obj) is a_class
