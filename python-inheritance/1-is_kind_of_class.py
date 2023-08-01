'''
This module defines a function that returns True if the object is an instance of, or if the object is an 
instance of a class that inherited from, the specified class ; otherwise False.
'''


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if the object is an instance of a class that inherited from,
    the specified class.

    Parameters:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of, or if the object is an instance of a class that inherited from,
        the specified class; otherwise, False.
    """
    return isinstance(obj, a_class)
