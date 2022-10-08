"""
Given an `append_value()` function, accept a list of numbers and append the value `6` to the end of the list.
"""


def append_value(nums):
    """using append() method"""
    nums.append(6)
    return nums
    """using + operator"""
    # nums = nums + [6]
    # return nums


print(append_value([1, 2, 3, 4, 5]))
