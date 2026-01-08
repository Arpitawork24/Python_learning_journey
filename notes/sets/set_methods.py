# if a nd b sets are there
#union → new set like c
#update → update existing set like a

A = {1, 2, 3}
B = {3, 4, 5}

C = A.union(B) #unionn of a nd b ; a or b isnt changed
print(C) #new set k/a c is created
print(A) #here a isnt changed

A.update(B) #updating a
print(A) #here a is changed or updated
