#!/usr/bin/python3
def validate_password(password):

    if len(password) < 8:
        return False

    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

        # Check for spaces
        if char.isspace():
            return False

    return has_uppercase and has_lowercase and has_digit


print(validate_password("Abc123"))      # Output: True
print(validate_password("Hello123"))    # Output: True
print(validate_password("password"))    # Output: False (No uppercase)
print(validate_password("abcd1234"))    # Output: False (No uppercase)
print(validate_password("SecurePass"))  # Output: False (No digit)
print(validate_password("Pass word1"))  # Output: False (Contains space)
