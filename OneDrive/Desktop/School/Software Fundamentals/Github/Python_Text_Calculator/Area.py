# Area.py

from math import pi

# Contains Area Calculating Functions

def area_of_square(side: float) -> float:
    """Calculates the area of a square."""
    return side * side

def area_of_circle(radius: float) -> float:
    """Calculates the area of a circle."""
    return pi * (radius ** 2)

def area_of_triangle(base: float, height: float) -> float:
    """Calculates the area of a triangle given its base and height."""
    return 0.5 * base * height

def area_of_rectangle(length: float, width: float) -> float:
    """Calculates the area of a rectangle."""
    return length * width