import random as rd

print("1= rock, 2=paper, 3= scissor")
while True :
    a = int(input("enter the no.= "))
    b = rd.randint(1,3)
    print(b)
    
    if a == b :
        print("draw")
    elif a == 1 and b == 2:
        print("u lose")
    elif a == 1 and b == 3:
        print("u win")
    elif a == 2 and b == 1:
        print("u win")
    elif a == 2 and b == 3:
        print("u lose")
    elif a == 3 and b == 1:
        print("u lose")
    elif a == 3 and b == 2:
        print("u win")
    else :
        print("error")
    

