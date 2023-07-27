#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        print()

    for row in matrix:
        if not row:
            print()
            continue

        for i, num in enumerate(row):
            if i == len(row) - 1:
                print("{:d}".format(num**2))
            else:
                print("{:d} ".format(num), end="")
