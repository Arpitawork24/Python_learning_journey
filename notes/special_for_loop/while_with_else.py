#theory -
# The else block appears after the body of the loop.
i = 0
while i < 7:
    print(i)
    i=i+1

else :
    print("while loop is over \n") #after while loop is completed this will run.

#useless else with while loop
i = 0
while i < 7:
    print(i)
    i=i+1
    if i==4:
        break
else :
    print("while loop is over\n \n") #this else loop wont run bcz for loop was broken or not completed fully


#useful else with while loop
print("last example \n")

i = 0
while i < 7:
    i=i+1
    if i==9:
        break
else :
    print("while loop is over")