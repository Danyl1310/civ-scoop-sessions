#Imports
from animal import Animal


#Subclass Dog
class Dog(Animal):
    def __init__(self, species, name):
        super().__init__(species = "Canis familiaris")
        self.subspecies = species
        self.is_mammal = True
        self.legs = 4
        self.has_tail = True
        self.name = name
    
    def walk(self, destination):
        print(f"{self.name}: Walks to {destination}")

    def speak(self):
        print(f"{self.name}: *Barks*")