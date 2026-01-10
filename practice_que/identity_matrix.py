# Identity Matrix Pattern
# An identity matrix is a square matrix in which all the elements of the principal diagonal are ones, and all other elements are zeros.
n = int(input("Enter the size of the identity matrix: "))

for i in range(n):
    for j in range(n):
        if i == j:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()  # Move to the next line after each row