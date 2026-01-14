#Dictionaries are ordered collection of data items.
#they are are key-value pairs
roll = {
    1 : "Arpita",
    2: "Piyu",
    3: "Raj",
    4 : "cutiee",
    5 : "sweetu"
}

print(roll) #printing all key with their values
print("only values-",roll.values()) #this will print all values only without key
print("only keys-",roll.keys()) #this will print all keys only without values
print("all key-values-\n",roll.items()) #this will print all keys nd values pairs
print(roll[2]) #accessing value of (key) roll no 2 as 2 is key
# print(roll["Piyu"]) #this will give error bcz piyu is key nd in dict only values can be accessed using key
print(roll.get(1)) #can also be accessed using get method

#print(roll.update({3: "Rahul"})) # this will give o/p as none as update do updates but returns none only
(roll.update({3: "Rahul" , 1: "Sanu"})) #updating 2 values
print(roll) #updated

roll.pop(3) #popped key-value pair whose key is mentioned i.e. 3
print(roll)
roll.popitem()
print(roll) #pops last key-value pair
del roll[2] #del keyword can be used like the pop()
print(roll)

roll.clear()
print(roll) #dict cleared

#eg-2

result = {
    "Arpita" : 80,
    "Rohan" : 54,
    "Piyu" : 85
    
}

print("Result-\n",result) #accessing all result
print(result["Rohan"]) #accessing rohan's result as rohan is key
print(result.get("Arpita"))