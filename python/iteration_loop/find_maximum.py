"""
Find the maximum value in a list of numbers.
"""


def find_maximum(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


print(find_maximum([1, 2, 3, 4, 5]))
