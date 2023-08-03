'''
This module is an empty class.
'''


class MyNewClass:
    '''
    Simple empty class 
    Contains a function tha excludes the attribute 
    __init_subclass_ from dir()
    '''

    def __dir__(cls) -> None:
        # get list of all attributes for this class and exclude __init_subclass
        attributes = super().__dir__()

        list_to_return = []

        for attr in attributes:
            if attr != "__init_subclass__":
                # append this to the list_to_return
                list_to_return.append(attr)

        return list_to_return
