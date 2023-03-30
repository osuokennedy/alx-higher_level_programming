#!/usr/bin/python3
"""define a class Square."""
class Square:
    """ Represent A square."""
    def __init__(self, size = 0):
        """ Initialize new square
        Args:
        size (int): The size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("sixe must be >=0")
        self.__size=size
