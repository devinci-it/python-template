class {class_name}:
    '''
    A brief description of the class.

    Attributes:
        attribute1 (int): Description of attribute1.

    Methods:
        __init__ (method): Constructor method.
        attribute1 (property): Getter and setter method for attribute1.
        __str__ (method): String representation method.
        __repr__ (method): Printable representation method.
        get_methods (method): Returns a list of all methods in the class.
    '''

    def __init__(self) -> None:
        '''
        Initializes the class.
        '''
        self._attribute1: int = 0

    def __str__(self) -> str:
        '''
        Returns a string representation of the object.
        '''
        pass

    def __repr__(self) -> str:
        '''
        Returns a printable representation of the object.
        '''
        pass

    @property
    def attribute1(self) -> int:
        '''
        Gets the value of attribute1.

        Returns:
            int: The value of attribute1.
        '''
        return self._attribute1

    @attribute1.setter
    def attribute1(self, value: int) -> None:
        '''
        Sets the value of attribute1.

        Args:
            value (int): The value to set.
        '''
        self._attribute1 = value

    def get_methods(self) -> list:
        '''
        Returns a list of all methods in the class.

        Returns:
            list: A list of method names.
        '''
        methods = [func for func in dir(self) if
                   callable(getattr(self, func)) and not func.startswith("__")]
        return methods
