try :
    num = int(input("enter num = "))
    a = [6,8,4]
    print(a[num])
except ValueError:  #if num = kgf (not integer)
    print("value error")
except IndexError:  #if num = 5 (index that doesn't exist rn)
    print("index error")