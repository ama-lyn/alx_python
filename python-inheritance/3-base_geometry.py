'''
This module is an empty class.
'''


class BaseGeometry:
    '''
    Empty class 
    '''

    def __dir__(self):
        # Get list of all attributes for this instance and exclude __init_subclass__
        attributes = super().__dir__()

        return [attribute for attribute in attributes if attribute != '__init_subclass__']
