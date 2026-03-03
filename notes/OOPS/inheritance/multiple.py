class Employee():
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"name is {self.name}")

class Dancer():
    def __init__(self, dance):
        self.dance = dance
    def show(self):
        print(f"dance is {self.dance}")

class EmpDanc(Employee, Dancer):
    def __init__(self, name,dance):
        self.name = name
        self.dance = dance
    
o = EmpDanc("raj","kathak")
print(o)
o.show()  # method will run of the parent class which is accessed firstly in the child class like here Employee is called or accessed first.

# MRO (Method Resolution Order) in Python, which defines the order in which a class searches for methods in its parent classes
print(EmpDanc.mro()) 