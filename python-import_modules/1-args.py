#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Get the number of arguments
    num_arguments = len(sys.argv) - 1

    # Print the number of arguments
    if num_arguments == 0:
        print("0 arguments.")
    elif num_arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_arguments))

    # Print the list of arguments and their positions
    for i in range(1, num_arguments + 1):
        print("{}: {}".format(i, sys.argv[i]))
