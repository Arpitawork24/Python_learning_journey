# You are given a list that contains integers. You need to decrement each element of the list by 1 and return the list.

def decre(arr):
    for i in range(len(arr)):  #this is used when - you need to modify the list , you need to modify the list
        arr[i]=arr[i]-1
    return (arr)

print(decre([5,3,7,2]))