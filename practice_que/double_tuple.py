def doubleTup(numbers):
    #code here
    temp = list(numbers)
    for i in range(len(temp)):  #this is used when - you need to modify the list , you need indices.
        temp[i]=temp[i]*2
    numbers = tuple(temp)
    return(numbers)

print(doubleTup((2,5,7,8)))