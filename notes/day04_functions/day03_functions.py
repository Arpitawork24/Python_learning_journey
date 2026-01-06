#basic example-
def gmean(a,b):
    print("gmean")
    return (a*b)/(a+b)
print(gmean(a=9,b=8))
print(gmean(2,4))

#functions are positional-
def name(fname,lname):
    print("first name is -",fname)
    print("last name is -", lname)

name("arpita","sutariya")
name("sutariya","arpita")