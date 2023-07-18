#!/usr/bin/python3
def is_prime(number):
    if number == 2:
        return True
    elif number < 2 or number % 2 == 0:
        return False
    else:
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True


print(is_prime(2))   # Output: False (2 is not prime)
print(is_prime(3))   # Output: True (3 is prime)
print(is_prime(11))  # Output: True (11 is prime)
print(is_prime(20))  # Output: False (20 is not prime)
print(is_prime(23))  # Output: True (23 is prime)
