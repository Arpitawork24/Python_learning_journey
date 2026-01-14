def doubleTup(numbers):
    #code here
    temp = list(numbers)
    for i in range(len(temp)):
        temp[i]=temp[i]*2
    numbers = tuple(temp)
    return(numbers)

print(doubleTup((2,5,7,8)))