"""
Calculate the average value of a nested dictionary.
"""


def average_value(d):
    total = 0
    for sd in d.values():
        total += sum(sd.values()) / len(sd)
    return total / len(d)


print(average_value(
    {1: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}, 2: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}, 3: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}}))
