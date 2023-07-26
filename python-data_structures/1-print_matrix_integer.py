#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in matrix:
            print("{:d}".format(num), end=" ")
        print()
