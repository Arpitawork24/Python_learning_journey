#A frozenset in Python is a built-in data type that is similar to a set but with one key difference that is immutability. This means that once a frozenset is created, we cannot modify its elements that is we cannot add, remove or change any items in it. 
#Like regular sets, a frozenset cannot contain duplicate elements.
#If no parameters are passed, it returns an empty frozenset.  
# these are immutable like tuples ( i understood this)

fset = frozenset([1,4,6,2,8])
print(fset)

fset2 = {22,33,55,77,22,88,44}
print(frozenset(fset2))
