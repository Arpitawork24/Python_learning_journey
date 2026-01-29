# map, filter and reduce are built in func
# they are higher order functions as they take other func as arguments

# The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements.
# syntax - map(function, iterable)

def cube(x):
    return x*x*x

l = [1,2,3,4,5]

# for val in l:
#     print (val*val*val, end=" ")

# newl = []
# for item in l :
#     newl.append(cube(item))
# print(newl)

newl = list(map(cube,l))
print(newl)

# FILTER
# The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate.
#syntax - filter(predicate, iterable)

def fl(x):
    return x>3
l2 = list(filter(fl,l))
print(l2)