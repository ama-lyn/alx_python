'''
This module defines a class that raises an Exception with the 
message area() is not implemented
'''


class BaseGeometry:
    '''
    Simple class that raises an exception
    '''

    def area(self):
        raise Exception("area() is not implemented")
