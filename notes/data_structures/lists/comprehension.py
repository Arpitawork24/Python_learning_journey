a = [1,2,3,4,5]
# this will only print elements twice not double it
print(a*2)

#to print double of all elements 
res = [val * 2 for val in a]
print(res)

res2 = [val for val in a if val%2==0]
print(res2)

#creating a list from range
b = [ i for i in range(1,10)]
print(b)

c = [(x,y) for x in range(2) for y in range(3)]
print(c)

# Flattening a list of lists
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res3 = [val for row in mat for val in row]
print(res3)

#same logic without list comprehension
# res3 = []

# for row in mat:
#     for val in row:
#         res3.append(val)

# print(res3)
