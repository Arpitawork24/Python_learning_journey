# map, filter and reduce are built in func
# they are higher order functions as they take other func as arguments

# MAP
# The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements.
# syntax - map(function, iterable)
# It returns a map object, so usually we do:
# list(map(function, iterable))


def cube(x):
    return x*x*x

numbers = [1,2,3,4,5]

# for val in numbers:
#     print (val*val*val, end=" ")

# newl = []
# for item in numbers :
#     newl.append(cube(item))
# print(newl)

newl = list(map(cube, numbers))
print(newl)

# FILTER
# The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate.
#syntax - filter(predicate, iterable)

def fl(x):
    return x>3
l2 = list(filter(fl,numbers))
print(l2)

# REDUCE
# The reduce function is a higher-order function that applies a function to a sequence and returns a single value. It is a part of the functools module in Python
# It keeps combining elements
# syntax - reduce(function, iterable)

from functools import reduce

mysum = reduce(lambda x,y : x+y,numbers)
print(mysum)