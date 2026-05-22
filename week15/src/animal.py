#Imports
from abc import ABC, abstractmethod


#Abstract Class Animal
class Animal(ABC):
    def __init__(self, species):
        self.species = species
        self.subspecies = ""
        self.is_mammal = None
        self.legs = 0
        self.has_tail = None
    
    @abstractmethod
    def walk(self):
        raise NotImplementedError
    
    @abstractmethod
    def speak(self):
        raise NotImplementedError