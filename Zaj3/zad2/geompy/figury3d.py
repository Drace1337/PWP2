import math


def cube_volume(edge):
    return edge**3


def cube_surface_area(edge):
    return 6 * (edge**2)


def cuboid_volume(length, width, height):
    return length * width * height


def cuboid_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)


def sphere_volume(radius):
    return (4 / 3) * math.pi * radius**3


def sphere_surface_area(radius):
    return 4 * math.pi * radius**2
