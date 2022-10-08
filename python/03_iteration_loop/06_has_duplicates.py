"""
Check if a list has duplicates, the duplicates can be not contiguous.
"""


def has_duplicates(numbers):
    for i in range(len(numbers)):
        num = numbers[i]
        for num2 in numbers[i + 1:]:
            if num == num2:
                return True
    return False


print(has_duplicates([1, 2, 3, 4, 5]))
