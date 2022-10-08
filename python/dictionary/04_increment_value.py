"""
Accept a number `n` and increment dictionary values by `n`.
"""


def increment_value(d, n):
    for key in d:
        d[key] += n
    return d


print(increment_value({1: 1, 2: 2, 3: 3, 4: 4, 5: 5}, 5))
