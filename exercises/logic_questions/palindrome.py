# Program to check whether a number is a palindrome

# Take input from the user
num = int(input("Enter number: "))

# Store the original number in a temporary variable
temp = num

# Variable to store the reversed number
rev = 0

# Loop to reverse the number
while num > 0:
    # Get the last digit of the number
    digit = num % 10

    # Add the digit to the reversed number
    rev = rev * 10 + digit

    # Remove the last digit from the number
    num //= 10

# Check if the original number is equal to the reversed number
if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
