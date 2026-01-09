words = {"hii", "Arpita", "bird", "bad", "nice"}

for item in words :
    if item == "bad":
        break
    print(item) #this will print unordered as words is a kind of set
    
for i in range(6):
    if i >3 :
        break
    print(i)

print("----------")

for i in range(6):
    if i == 3 :
        break
    print(i)

print("----------")

for i in range(6):
    if i == 3 :
        continue
    print(i)

