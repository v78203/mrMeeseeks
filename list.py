from .check import is_list


def merge(*args):
    output_list = []
    for arg in args:
        if not is_list(arg):
            raise TypeError("input must be all lists")
        output_list += arg
    return output_list
