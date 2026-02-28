#basic example-
def gmean(a,b):
    print("gmean")
    return (a*b)/(a+b)
print(gmean(a=9,b=8))
print(gmean(2,4))

#functions are positional-
def name(fname,age):
    print("first name is -",fname)
    print("age is -", age)

name("arpita","20")
name("20","arpita")