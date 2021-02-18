import math


def sphere_area(radius):
    area = 4 * math.pi * radius * radius
    return area


def sphere_perimeter(radius):
    perimeter = (4. / 3) * math.pi * radius * radius * radius
    return perimeter
