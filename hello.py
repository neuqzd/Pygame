#!/usr/bin/env python

"""
A simple Python script to say hello.
--------------------------------------------
author: Jackson
email: gonglisuozcd@gmail.com
GitHub address: https://github.com/neuqzd
--------------------------------------------
********************************************
Usage:
    python hello.py [name]
********************************************
"""

import os
import sys

def usage():
    print(__doc__)
    sys.exit(-1)

def say_hello(name):
    my_name = str(name).strip()
    if not my_name[0].isalpha():
        print("This is NOT a name!")
    else:
        print("Hello, %s! Nice to meet you! I'm Jackson." % my_name)

def main():
    args = sys.argv[1:]
    if len(args) > 1:
        usage()
    else:
        if len(args) == 1:
            name = args[0]
        else:
            name = input("Please enter your name:")
        say_hello(name)

if __name__ == "__main__":
    # import pdb
    # pdb.set_trace()
    main()
    os.system("exit")