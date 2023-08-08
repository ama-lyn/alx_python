'''
Square Module - Contains the Square class that inherits from Rectangle
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    A class Square inherits from class Rectangle
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        Initialize a new Square instance

        Args:
            size (int): The size of the square's sides
            x (int): The x coordinate of the top left corner
            y (int): The y coordinate of the top left corner
            id (int): The id of the square
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for wsize."""

        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of this object with new values passed as arguments to this function
        Args:
        *args: Variable length argument list containing attributes in order:
            - 1st argument: id attribute
            - 2nd argument: width attribute
            - 3rd argument: height attribute
            - 4th argument: x attribute
            - 5th argument: y attribute
        **kwargs: Variable length keyword argument list containing attribute names and values.    
        """

        attributes = ['id', 'width', 'height', 'x', 'y']

        if args:
            for index, value in enumerate(args):
                if index < len(attributes):
                    setattr(self, attributes[index], value)

        if kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def __str__(self):
        """
        Returns the string representation of the Square instance

        Returns:
            str: [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
