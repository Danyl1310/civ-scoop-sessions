#Imports
from animal import Animal


#Subclass Cat
class Cat(Animal):
    def __init__(self, species, name):
        super().__init__(species = "Felis catus")
        self.subspecies = species
        self.is_mammal = True
        self.legs = 4
        self.has_tail = True
        self.name = name
    
    def walk(self, destination):
        print(f"{self.name}: silently and swiftly moves to {destination}.")

    def talk(self):
        print(f"{self.name}: *Meows*.")