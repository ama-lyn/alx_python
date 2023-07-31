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
    # Retrieve the current size of the square
    # Returns:
    # int: The size of the square.
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Parameters:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character #.

        If size is equal to 0, print an empty line.
        """
        if self.__size == 0:
            print()

        else:
            for _ in range(self.__size):
                print("#" * self.__size)
