#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
newNum = number
if number < 0:
    newNum *= -1

ld = newNum % 10
if ld > 5:
    print("{} {} is {} and is greater than 5".format(str, number, ld))
elif ld == 0:
    print("{} {} is {} and is 0".format(str, number, ld))
elif ld < 6 and not 0:
    print("{} {} is {} and is less than 6 and not 0".format(str, number, ld))
    
