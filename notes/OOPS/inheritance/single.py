class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def makesound(self):
        print("it makes sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "dog")   # fixed
        self.breed = breed

    def makesound(self):
        print("bark")

d = Dog("robo", "local")
d.makesound()

a = Animal("cutu", "cat")   # fixed
a.makesound()