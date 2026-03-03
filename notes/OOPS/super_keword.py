# super keyword is used to access methods or constructors of parent class from the child class.
# simply - It lets the child class use things from the parent class.

class Parent_class():
    def parent_method(self):
        print("this is parent method 1")
        
class Child_class(Parent_class):
    def child_method(self):
        print("this is child method 2")
        super().parent_method()
    
a = Child_class()
a.child_method()