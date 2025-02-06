#!/usr/bin/python

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for geometric shapes.
    It enforces the implementation of the 'area' and 'perimeter' methods in any subclass.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        Must be implemented by any subclass of Shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        Must be implemented by any subclass of Shape.
        """
        pass


class Circle(Shape):
    """
    Circle class that inherits from Shape.
    It represents a circle with a specified radius.
    """

    def __init__(self, radius):
        """
        Initializes the circle with a given radius.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculates the perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape.
    It represents a rectangle with a specified width and height.
    """

    def __init__(self, width, height):
        """
        Initializes the rectangle with given width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 7)

    print("Circle Info:")
    shape_info(circle)

    print("\nRectangle Info:")
    shape_info(rectangle)
