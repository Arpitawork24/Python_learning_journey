# Sets are unordered collection of data items nd do not contain duplicate items.
info = {"Carla", 19, False, 5.9, 19} #here 19 will print only once
print(info) # in 1 line with tuple format
for item in info:  # each word in new line
    print (item)

# remove() method removes a specified element from the set
#TypeError: set.remove() takes exactly one argument , if the element not found then remove() will raise error
info.remove("Carla")
print("remove-",info)

#discard() method also removes a specified element from the set. Unlike remove(), if the element is not found, it does not raise an error.
info.discard(5.9)
print(info)

print("info 1- ")
#they cannot be accessed using index numbers.
#accessing using for loop
info1 = {"Carla", 19, False, 5.9}

a,b,c,d = info1
print(a)
print(b)
print(c)
print(d)

for item in info1:
    print(item)

# pop() method removes nd returns an arbitary (random) element from the set ; although in list it always removes the last elemnent
val = info1.pop()
print(val)
print(info1)
