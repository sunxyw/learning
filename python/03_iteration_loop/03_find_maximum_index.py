"""
Find the index of the maximum value in a list of numbers.
"""


def find_maximum_index(numbers):
    maximum = numbers[0]
    index = 0
    for i in range(len(numbers)):
        if numbers[i] > maximum:
            maximum = numbers[i]
            index = i
    return index


print(find_maximum_index([1, 2, 3, 4, 5]))
