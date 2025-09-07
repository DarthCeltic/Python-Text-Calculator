# Volume.py

from math import pi

# Contains Volume Calculating Functions

def volume_of_cube(side: float) -> float:
    """Calculates the volume of a cube."""
    return side ** 3

def volume_of_cuboid(length: float, width: float, height: float) -> float:
    """Calculates the volume of a cuboid."""
    return length * width * height

def volume_of_cylinder(radius: float, height: float) -> float:
    """Calculates the volume of a cylinder."""
    return pi * (radius ** 2) * height

def volume_of_sphere(radius: float) -> float:
    """Calculates the volume of a sphere."""
    return (4/3) * pi * (radius ** 3)

def volume_of_cone(radius: float, height: float) -> float:
    """Calculates the volume of a cone."""
    return (1/3) * pi * (radius ** 2) * height