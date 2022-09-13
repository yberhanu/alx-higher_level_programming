#!/usr/bin/python3
""" Create Class for square and add Exeception to size """

class Square:
    """ Class with Init method and Exeception try / execpt """
    def __init__(self, size=0):
        """ initialization """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
