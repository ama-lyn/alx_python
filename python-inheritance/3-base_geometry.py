'''
This module is an empty class.
'''


class BaseGeometry:
    '''
    Empty class 
    '''
    pass
attributes = [attr for attr in dir(BaseGeometry) if attr != '__init_subclass__']
print(attributes)