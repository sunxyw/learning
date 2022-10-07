"""
Write a `calculate_sin_cos_tan()` function that takes a number as argument and returns the sine, cosine, and tangent
"""

import math


def calculate_sin_cos_tan(number):
    return math.sin(number), math.cos(number), math.tan(number)


print(calculate_sin_cos_tan(1))
