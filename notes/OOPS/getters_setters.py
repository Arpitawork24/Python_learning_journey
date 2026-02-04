class Student:
    def __init__(self, marks): # constructor
        self._marks = marks

    @property   # decorator for getter
    def marks(self):        # getter   # marks is now a property, not a normal function anymore.
        return self._marks

    @marks.setter   #@marks.setter is a decorator -> This method is the setter for the property called marks
    def marks(self, value):  # setter
        if value <= 0:
            print("Invalid marks")
        else:
            self._marks = value
s = Student(80)
print(s.marks)     # getter
s.marks = 90       # setter
print(s.marks)  
s.marks = 0     
print(s.marks)  