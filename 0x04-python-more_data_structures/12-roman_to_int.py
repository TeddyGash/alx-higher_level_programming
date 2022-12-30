#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
    integer = 0
    for i in range(len(roman_string)):
        if (i == (len(roman_string) - 1)):
            integer += roman_dict[roman_string[i].lower()]
        elif (roman_dict[roman_string[i].lower()] < roman_dict[roman_string[i + 1].lower()]):
            integer -= roman_dict[roman_string[i].lower()]
        else:
            integer += roman_dict[roman_string[i].lower()]
    return integer
