#!/usr/bin/python3

import sys


def display_args():
    """
    Command Quest: Displays the program name and command-line arguments.

    Prints the total number of arguments and lists each argument passed
    when running the script from the command line.
    """

    print("=== Command Quest ===")

    args_len = len(sys.argv)
    if args_len == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {args_len}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {args_len - 1}")
        i = 1
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1
        print(f"Total arguments: {args_len}")


if __name__ == "__main__":
    display_args()
