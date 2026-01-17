#tuple is an immutable ordered collection of elements
tup = (1, 2, 76, 342, 32, "green", True)
#tup[0] = 90 will give error as tuples are immutable
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34]) will give error as there is no index as 34 in tup

if  342 in tup:
    print("Yes 342 is present in this tuple")
tup2 = tup[1:4]
print(tup2)