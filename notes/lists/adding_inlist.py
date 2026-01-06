a = []

a.append(10)
print("After append(10):", a)

a.insert(0, 5) #insert 5 at index 0
print("After insert(0, 5):", a)

a.extend([15, 20, 25])
print("After extend([15, 20, 25]):", a)

a.reverse()
print(a)

a.clear()
print("After clear():", a)