# * = Collect all remaining elements into a list.
tup = (1,2,3,4,5)
a,*b,c = tup
print (a) #1st element
print(*b) # in between elements
print(c)  #last element

print("new")
a, b, *c = tup
print(a) #1st element
print(b) #2nd element
print(c) #remaining elements

# imp = only 1 * is allowed
#Enough elements must exist

print("new")
*a, b, c = tup
print(*a) #all except last 2
print(b) #2nd element
print(c) #last elements
