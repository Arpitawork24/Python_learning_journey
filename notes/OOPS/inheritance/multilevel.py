# Example of multilevel inheritance
# Animal → Dog → Local

class Animal():
    def __init__(self, name, species):
        # Constructor of base class
        # Initializes common attributes for all animals
        self.name = name
        self.species = species
        
    def show_details(self):
        # Displays basic animal information
        print(f"name : {self.name}")
        print(f"species : {self.species}")


class Dog(Animal):
    def __init__(self, name, breed):
        # Calling the constructor of the parent class (Animal)
        # Species is fixed as "Dog"
        Animal.__init__(self, name, species="Dog")
        self.breed = breed  # Dog-specific attribute

    def show_details(self):
        # First show details from the Animal class
        Animal.show_details(self)
        # Then show additional details specific to Dog
        print(f"breed : {self.breed}")


class Local(Dog):
    def __init__(self, name, color):
        # Calling constructor of Dog class
        # Breed is fixed as "local"
        Dog.__init__(self, name, breed="local")
        self.color = color  # Local dog specific attribute

    def show_details(self):
        # First show Dog (and Animal) details
        Dog.show_details(self)
        # Then show additional detail specific to Local class
        print(f"color : {self.color}")
    

# Creating an object of the most derived class
dog = Local("Max", "Golden")

# Calling the method to display details
# This will show Animal → Dog → Local details
dog.show_details()