# argparse helps you design a proper command-line program.

import argparse

# You are creating an argument manager.
parser = argparse.ArgumentParser()

# Here you are telling Python: My program expects an argument called arg1
parser.add_argument("arg1", help="desc of arg 1")
parser.add_argument("arg2", help="desc of arg 2")

# This line collects the arguments from the command line.
args = parser.parse_args()

print(args.arg1)
print(args.arg2)
