#theory -
# The else block appears after the body of the loop.
i = 0
while i < 7:
    print(i)
    i=i+1

else :
    print("while loop is over \n") #after for loop is completed this will run.


i = 0
while i < 7:
    print(i)
    i=i+1
    if i==4:
        break
else :
    print("while loop is over") #this else loop wont run bcz for loop was broken or not completed fully