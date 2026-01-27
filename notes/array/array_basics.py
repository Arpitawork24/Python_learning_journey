import array as arr

#i = integer only
a = arr.array("i",[1,3,4,2,10,3,6])

#accessing element through index
print(a[0])

#appending 
a.append(5)
print(a)

for i in range(3):
    print(a[i], end=" ")

#adding elements to array
a.insert(7,8)
print(a)

# removing first occurence of element (not index)
a.remove(3)
print(a)

#removing element at index 3
a.pop(3)
print(a)