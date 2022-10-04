"""
Determines whether a given pair (x, y) falls in the range (x < 1/3 < y).
Returns True if x < 1/3 < y; otherwise, it returns False.
"""


def check_in_range(x, y):
    return x < (1 / 3) < y


print(check_in_range(0, 1))
