"""
Find a value in a nested dictionary which match the given pattern, and return the key that corresponds to it.
"""


def find_value(d, pattern):
    for key, dd in d.items():
        if dd['name'] == pattern:
            return key

    return None


print(find_value({1: {'name': 'John'}, 2: {'name': 'Jane'}, 3: {'name': 'Jack'}}, 'Jane'))
