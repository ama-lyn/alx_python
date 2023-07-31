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

    def __init__(self, size=0):
        self.__size = size
        """
       Initialize a Square instance with a given size.

       Parameters:
           size (int): The size of the square.
       """

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return pow(self.__size, 2)
