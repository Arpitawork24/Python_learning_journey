class Person():
    name = "Arpita"
    occupation = "SWE"
    age = 20
    def info(self):
        print(f"{self.name} is {self.occupation}")

a = Person()  # will give default values if not mentioned seperately
b = Person()
c = Person()
b.name = "Rohan"
b.occupation = "Webdev"

a.info()
b.info()
c.info()