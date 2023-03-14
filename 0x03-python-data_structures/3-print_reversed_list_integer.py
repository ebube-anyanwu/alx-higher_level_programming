#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if len(my_list) > 1:
        for ints in my_list[::-1]:
            print("{}".format(ints))
    else:
        print("{}".format(my_list[0]))
