#!/usr/bin/python3
"""A function that replaces an element of a list in a specific position"""


def replace_in_list(my_list, idx, element):
     if 0 <= idx < len(my_list):
        my_list[idx] = element
    return(my_list)
