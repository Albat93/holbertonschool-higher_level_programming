#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Exclude the script name
    argc = len(argv)  # Count the number of arguments

# Determine the correct wording for "argument(s)"
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))

# Print each argument with its position
    for i, arg in enumerate(argv, 1):
        print("{}: {}".format(i, arg))
