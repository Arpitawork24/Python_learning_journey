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

#at a particular index adding elements to array
a.insert(7,8)
print("insert",a)

# removing first occurence of element (not index)
a.remove(3)
print(a)

#removing element at index 3
a.pop(3)
print(a)

# index of 1st occurrence of 6
print(a.index(6))

# update item at index 2
a[2] = 6
print(a)

# count() method to count given item in array.
count = a.count(6)
print(count)

# reverse
a.reverse()
print(*a)

#  The extend() function is simply used to attach an item from iterable to the end of the array
a.extend([6,7,8,9,2])
print(a)