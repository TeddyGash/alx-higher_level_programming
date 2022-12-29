#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_L = []
 
    for i in range(len(my_list)):
        if (my_list[i] == search):
            new_L.append(replace)
        else:
            new_L.append(my_list[i])
    return new_L
