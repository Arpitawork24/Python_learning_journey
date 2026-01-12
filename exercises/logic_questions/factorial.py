# a type of recursive function

def factorial(n):
    if n == 0:  # Base case
        return 1
    else:        # Recursive case
        return n * factorial(n - 1)

print(factorial(4))

# Base Case: When n == 0, recursion stops and returns 1.
# Recursive Case: Multiplies n with the factorial of n-1 until it reaches the base case.