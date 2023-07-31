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
