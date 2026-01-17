a = input("enter the num= ")

try:  # when this is applied even if the code below gives error the code will run
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except Exception as e :     #or except:
    print(e)                    #or print("error occured")

print("end")
