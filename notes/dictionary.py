#Dictionaries are ordered collection of data items.
#they are are key-value pairs
roll = {
    1 : "Arpita",
    2: "Piyu",
    3: "Raj"
}

print(roll) #printing all key with their values
print(roll.values()) #this will print all values only without key
print(roll.keys()) #this will print all keys only without values
print(roll.items()) #this will print all keys nd values pairs
print(roll[2]) #accessing value roll no 2 as 2 is key
# print(roll["Piyu"]) #this will give error bcz piyu is key nd in dict only values can be accessed using key
print(roll.get(1)) #can also be accessed using get method

Result = {
    "Arpita" : 80,
    "Rohan" : 54,
    "Piyu" : 85
    
}

print(Result) #accessing all result
print(Result["Rohan"]) #accessing rohan's result as rohan is key
print(Result.get("Arpita"))