# The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object.
x = [1,2,3]
print(dir(x))

# __dict__: The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection. 
class Person():
    def __init__(self,name, age):
        self.name = name
        self.age = age
p = Person("arpita",20)
print(p.name,p.age)
print(p.__dict__)

# help(): The help() function is used to get help documentation for an object, including a description of its attributes and methods. 
print(help(Person))
print(help(int))
print(help(str))
print(help(bool))