x = 5 # global var
print(x)

def hello():
    print("hii")
    y = 2
    print(y) # local var can be clld inside its func only
    print(x) # global var can be clld inside nd outside the func

hello()
print("x = ", x)
# print(y) this will not print as y is a local variable nd will only run inside its own func

def hiii():
    print("hiiiii")
    z = 4
    print(z)
    global x # this is to change the value of a global var x
    x = 2
hiii()
print(x)

# If you want to modify global variable inside function, you must use global keyword
a = 10

def change():
    global a  # to change global a
    a = 20

change()
print(a)