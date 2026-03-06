import sys

# sys.argv stores the command line inputs.
a = int(sys.argv[1])
b = int(sys.argv[2])

print(a + b)

# Using sys.argv directly has problems:

# Hard to manage many arguments
# No automatic help message
# No type checking
# Users can get confused about how to run the program