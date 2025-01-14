#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert to uppercase by subtracting difference in ASCII values
            print(chr(ord(char) - 32), end="")
        else:
            print(char, end="")
    print()  # Print a new line after the string
