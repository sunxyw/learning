"""
Calculate the average value of a dictionary.
"""


def average_value(d):
    return sum(d.values()) / len(d)


print(average_value({1: 1, 2: 2, 3: 3, 4: 4, 5: 5}))
