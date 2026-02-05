# Static methods in Python are methods that belong to a class rather than an instance of the class
# They are defined using the @staticmethod decorator. 
# They do not have access to the instance of the class (i.e. self). 

class Math():
    def __init__(self, num):
        self.num = num  #instance variables -> under __init__
    def add_n(self, n): # normal method -> needs "self"
        self.num += n   # normal method can access instance variables
    
    @staticmethod  # decorator for static method
    def add (a,b):
        return a + b
        

a = Math(5)  # a = object created 
print(a.num)
a.add_n(3)
print(a.num)
print(Math.add(5,3))  # this doesnt need object creation