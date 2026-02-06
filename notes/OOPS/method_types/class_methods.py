# these are bound to class nd not the instance of the class.
# used to change something that belongs to class (not a object)
class Employee():
    company = "apple"  #class variable
    def show(self):
        print(f"the name is {self.name} nd company is {self.company}")
    
    def changecomp(cls,newcomp):
        cls.company = newcomp
        
    @classmethod   # this decorator is used to define class method
    def changecomp2(cls2,newcomp2):
        cls2.company = newcomp2

s = Employee()
s.name = "rohit"
s.show()
s.changecomp("google")
s.show()
print(Employee.company)

s.changecomp2("aws")
s.show()
print(Employee.company)
