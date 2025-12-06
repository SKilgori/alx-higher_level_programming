#!/usr/bin/python3
"""My square module"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """Create a Square
        Args: size: length of a side of Square
        """
        self.__size = size

    @property
    def size(self):
        """"The propery of size as the len of a side of Square
        Raises:
            TypeError: if size != int
            ValueErrorr: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size - Function documentation.
        
        Args:
            self: Description of self.
            value: Description of value.
        
        Returns:
            Description of the return value.
        """
        """size - Function documentation.
        
        Args:
            self: Description of self.
            value: Description of value.
        
        Returns:
            Description of the return value.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Get the area of a Square
        Returns: The size squared
        """
        return self.__size * self.__size

    def __le__(self, other):
        """__le__ - Function documentation.
        
        Args:
            self: Description of self.
            other: Description of other.
        
        Returns:
            Description of the return value.
        """
        """__le__ - Function documentation.
        
        Args:
            self: Description of self.
            other: Description of other.
        
        Returns:
            Description of the return value.
        """
        return self.area() <= other.area()

    def __lt__(self, other):
        """__lt__ - Function documentation.
        
        Args:
            self: Description of self.
            other: Description of other.
        
        Returns:
            Description of the return value.
        """
        """__lt__ - Function documentation.
        
        Args:
            self: Description of self.
            other: Description of other.
        
        Returns:
            Description of the return value.
        """
        return self.area() < other.area()

    def __ge__(self, other):
        """__ge__ - Function documentation.
        
        Args:
            self: Description of self.
            other: Description of other.
        
        Returns:
            Description of the return value.
        """
        """__ge__ - Function documentation.
        
        Args:
            self: Description of self.
            other: Description of other.
        
        Returns:
            Description of the return value.
        """
        return self.area() >= other.area()

    def __ne__(self, other):
        """__ne__ - Function documentation.
        
        Args:
            self: Description of self.
            other: Description of other.
        
        Returns:
            Description of the return value.
        """
        """__ne__ - Function documentation.
        
        Args:
            self: Description of self.
            other: Description of other.
        
        Returns:
            Description of the return value.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """__gt__ - Function documentation.
        
        Args:
            self: Description of self.
            other: Description of other.
        
        Returns:
            Description of the return value.
        """
        """__gt__ - Function documentation.
        
        Args:
            self: Description of self.
            other: Description of other.
        
        Returns:
            Description of the return value.
        """
        return self.area() > other.area()

    def __eq__(self, other):
        """__eq__ - Function documentation.
        
        Args:
            self: Description of self.
            other: Description of other.
        
        Returns:
            Description of the return value.
        """
        """__eq__ - Function documentation.
        
        Args:
            self: Description of self.
            other: Description of other.
        
        Returns:
            Description of the return value.
        """
        return self.area() == other.area()
