#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    pos_number = number * -1
else:
    pos_number = number

last_digit = pos_number % 10

if (last_digit > 5):
    comment = "and is greater than 5"
elif (last_digit == 0):
    comment = "and is 0"
elif (last_digit < 6 and last_digit != 0):
    comment = "and is less than 6 and not 0"

print("Last digit of {} is {} ".format(number, last_digit) + comment)
