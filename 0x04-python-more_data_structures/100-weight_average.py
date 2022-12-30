#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) > 0:
        product_sum = 0
        weight_sum = 0
        for tuple in my_list:
            product_sum += (tuple[0] * tuple[1])
            weight_sum += tuple[1]
        average = product_sum / weight_sum
        return average
    else:
        return 0
