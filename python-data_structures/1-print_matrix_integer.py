#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()  # If the matrix is empty, print an empty line and return
        return

    for row in matrix:
        if not row:  # If the row is empty, print a new line and skip to the next row
            print()
            continue

        for i, num in enumerate(row):
            if i == len(row) - 1:
                print("{:d}".format(num))
            else:
                print("{:d} ".format(num), end="")
