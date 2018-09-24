class Pets:
    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())

class Dog:
    species = "mammal"
    is_hungry = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return self.name, self.age

    def eat(self):
        self.is_hungry = False

    def walk(self):
        return "{} is walking!".format(self.name)

class GermanShepherd(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

class RottWeiler(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Instances of dogs
my_dogs = [
    RottWeiler("Tom", 6), 
    GermanShepherd("Fletcher", 7), 
    Dog("Larry", 9)
]

my_pets = Pets(my_dogs)

my_pets.walk()