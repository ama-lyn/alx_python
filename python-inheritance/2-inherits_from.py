"""
This module uses `issubclass()` method for this purpose which checks whether
one class is derived.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or
    indirectly) from the specified class.

    Parameters:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class; otherwise, False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
