#Imports
import sys
from src.cat import Cat
from src.dog import Dog

sys.path.append("src")


cat = Cat("Maple")
dog = Dog("Maxi")

cat.speak()
dog.speak()

cat.walk(dog.name)
dog.walk(cat.name)
