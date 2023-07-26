#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Loop through each row of the matrix
    for row in matrix:
        # Create an empty string to store the formatted row
        row_str = ""
        # Loop through each element of the row
        for elem in row:
            # Use str.format() to add the element to the string with a fixed width of 3
            row_str += "{:3}".format(elem)
        # Print the row string
        print(row_str)
