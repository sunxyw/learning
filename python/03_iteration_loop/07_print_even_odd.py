"""
Print even and odd numbers decresingly.
"""


def print_even_odd(num):
    for i in range(num, 0, -1):
        if i % 2 == 0:
            print("Even: ", i)
        else:
            print("Odd: ", i)


print_even_odd(10)
