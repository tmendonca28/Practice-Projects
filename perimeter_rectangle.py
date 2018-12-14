"""
Find perimeter of rectangle
"""


def calculate_perimeter(width, height):
    perimeter = (2*int(width)) + (2*int(height))
    return perimeter


print(calculate_perimeter(4, 7))