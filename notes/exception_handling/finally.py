def func() :
    try:
        lis = [2,4,5,8,3]
        n = int(input("enter num = "))
        print(lis[n])
        return 1
    except:
        print("error")
        return 0
    finally:
        print("I'll always execute no matter what")
    
print(func())