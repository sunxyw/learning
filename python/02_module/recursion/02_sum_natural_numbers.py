"""
Compute the sum of the first n natural numbers.
"""


def sum_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural_numbers(n - 1)


print(sum_natural_numbers(10))
