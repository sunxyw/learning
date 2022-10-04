"""
Transform the string (three literals) in such a way that every literal is tripled respectively.
"""


def get_str(s):
    return ''.join([char * 3 for char in s])


print(get_str('abc'))
