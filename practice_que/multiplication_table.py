# Generate a multiplication table for numbers from 1 to a user-defined limit, showing all multiples from 1 to 10.
n = 5
for i in range(1,11):
    for j in range(1,n+1):
        print(i*j , end = '  ')
    print()