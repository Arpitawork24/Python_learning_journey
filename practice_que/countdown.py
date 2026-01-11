# Implement a countdown that starts from a user-given number and decreases to 1, displaying the remaining time at each step.

#imp - range(start, stop, step)

n = int(input("enter countdown seconds : ",))
for i in range (n,0,-1):
    print(i)

# or we can use while also-
# while n>0:
#     print(n)
#     n -=1