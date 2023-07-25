#!/usr/bin/python3
def add(a, b):
    return a + b


if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2

    result = add(a, b)

    # Print the result using string formatting
    print("{} + {} = {}".format(a, b, result))
