'''
This module defines a class that raises an Exception with the 
message area() is not implemented
'''


class BaseMetaClass(type):
    """
    overrides.
    """
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']


class BaseGeometry(metaclass=BaseMetaClass):
    """
   Simple empty class 
    Contains a function tha excludes the attribute 
    __init_subclass_ from dir()
    """
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''
    This is a simple class to represent a rectangle.

   Attributes:
       width: private attribute.
       height: private attribute.
       Inherited function-integer_validator
    '''

    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
