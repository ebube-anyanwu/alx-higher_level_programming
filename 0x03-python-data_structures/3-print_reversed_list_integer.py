#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if len(my_list) > 0:
        for ints in reversed(my_list):
            print("{}".format(ints))
