# Sets are unordered collection of data items nd do not contain duplicate items.
info = {"Carla", 19, False, 5.9, 19} #here 19 will print only once
print(info)

#they cannot be accessed using index numbers.
#accessing using for loop
info1 = {"Carla", 19, False, 5.9}
for item in info1:
    print(item)