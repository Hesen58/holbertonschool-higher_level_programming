#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1
    zor = number % 10
    print("{}".format(zor), end="")
    return zor
