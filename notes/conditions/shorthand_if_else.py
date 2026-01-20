a = 360
b = 20000
print("a") if a>b else print("=") if a == b else print("b")
print ("good") if a<b else ""
print ("bad") if a>b else "" # it wont print anything if the else statement is true here or its exectued

c = 9 if a<b else 0
print(c)