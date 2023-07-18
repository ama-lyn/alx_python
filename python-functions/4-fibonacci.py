#!/usr/bin/python3
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        for _ in range(2, n):
            next_number = sequence[-1] + sequence[-2]
            sequence.append(next_number)
        return sequence


print(fibonacci_sequence(10))
