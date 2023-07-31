"""
Module 0-square
This module defines a Square class with a private instance attribute 'size'.
"""


class Square:

    """
   This is a simple class to represent a square.

   Attributes:
       size: private attribute with no type/value verification
   """

    def __init__(self, size):
        """
       Initialize a Square instance with a given size.

       Parameters:
           size (int): The size of the square.
       """
        self.__size = size
