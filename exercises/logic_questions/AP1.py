def extendAP(arr):
    # code here
    d = arr[1]-arr[0]
    last = arr[-1]
    temp = list(arr)  #converted to list as tuple doesnt modify directly
    for _ in range(3):
        last = last + d
        temp.append(last)
    arr = tuple(temp)
    return arr

print(extendAP([3,5,7,9]))