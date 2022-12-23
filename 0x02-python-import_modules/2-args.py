#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    print("{} {}{}".format((len(argv) - 1), 'arguments' if len(argv) == 1 or len(argv) > 2 else 'argument', '.' if len(argv) == 1 else ':'))
    if (len(argv) > 1):
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
