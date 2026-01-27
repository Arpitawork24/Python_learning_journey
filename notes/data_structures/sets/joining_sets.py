# if a nd b sets are there
#union → new set like c
#update → update existing set like a

A = {1, 2, 3}
B = {3, 4, 5}

# Accessing element using For loop
for i in A:
    print(i)

# Checking the element# using in keyword prints true if present else false
print(1 in A)

C = A.union(B) #unionn of a nd b ; a or b isnt changed
print("union",C) #new set k/a c is created
print(A) #here a isnt changed

#The intersection() and intersection_update() methods prints only items that are similar to both the sets.
C = A.intersection(B)
print("inter",C)

A.update(B) #updating a
print("update",A) #here a is changed or updated

A = {1, 2, 3}
B = {3, 4, 5}

A.intersection_update(B)
print("inter_update",A)

A = {1, 2, 3}
B = {3, 4, 5}

# The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets.
C = A.symmetric_difference(B)
print("symm",C)

A.symmetric_difference_update(B)
print(A)

#The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. or "-" operator is used
A = {1, 2, 3}
B = {3, 4, 5}

C = A.difference(B)
print("diff",C)

A.difference_update(B)
print(A)
