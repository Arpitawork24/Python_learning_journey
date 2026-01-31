class Person():
    def __init__(self, n, o):
        # instance variables
        self.name = n
        self.occ = o
    def info(self):
        print(f"{self.name} is {self.occ}")
    
a = Person("Arpita", "SWE")
a.info()
# b= Person() # this will give error as no arg are present in b 
b = Person("RODO","WEBDEV")
b.info()
c = Person(1,2)
c.info()
# d = Person(1,2,3)
# d.info()  # this will give error as only 2 args are possible here.