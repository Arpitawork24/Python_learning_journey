#theory -
# The else block appears after the body of the loop.
for i in range(6):
    print(i)
else:
    print("no i or i is over") #after for loop is completed this will run.

for i in range(6):
    print(i)
    if i==3 :
        break;
else:
    print("no i or i is over") #after for loop is completed this will run.