"""
Find the largest value in a dictionary, and return the key that corresponds to it.
"""


def largest_value(d):
    return max(d, key=d.get)


print(largest_value({1: 1, 2: 2, 3: 3, 4: 4, 5: 5}))
