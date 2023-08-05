'''
This module is an empty class.
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
