x = int(input("enter: "))
match x:
    case 0 :
        print("0")
    case 1:
        print("1")
    case _ if x<50:
        print("less than 50")
    case _ :
        print(x)
        