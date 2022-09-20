#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """ rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ constructor """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ parameter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ This method returns the string representation of the object """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            t = "\n".join([str(self.print_symbol) * self.__width
                           for i in range(self.__height)])
            return t

    def __repr__(self):
        """ function returns the object representation in string format """
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """ Destructors """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """" Bigger or Equal """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ square """
        return (cls(size, size))
