#!/usr/bin/python3


def max_integer(my_list=[]):
    if (len(my_list) == 0):
        max = None
    elif (len(my_list) == 1):
        max = my_list[0]
    elif (len(my_list) > 1):
        max = my_list[0]
        for number in my_list:
            if (number > max):
                max = number
    return max
