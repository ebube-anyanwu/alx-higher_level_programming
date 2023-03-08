#!/usr/bin/python3

def print_last_digit(number):
    newNum = abs(number)
    lastDigit = newNum % 10

    print("{}".format(lastDigit), end='')
    return lastDigit
