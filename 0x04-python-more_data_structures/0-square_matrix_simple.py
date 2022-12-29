#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    sq_list = [[x**2 for x in row] for row in matrix]
    return sq_list
