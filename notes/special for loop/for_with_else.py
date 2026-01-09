#theory -
# The else block appears after the body of the loop.
for i in range(6):
    print(i)
else:
    print("no i or i is over\n") #after for loop is completed this will run.

for i in range(6):
    print(i)
    if i==3 :
        break;
else:
    print("no i or i is over") #this else loop wont run bcz for loop was broken or not completed fully