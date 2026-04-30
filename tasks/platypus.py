class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Bird(Animal):
    def make_sound(self):
        return "kwikwi"

# Instantiation
dog = Dog("Rex")
cat = Cat("Felix")
bird = Bird("Skye")

# Simple prints without f-strings
print(dog.name, "makes sound", dog.make_sound())
print(cat.name, "makes sound", cat.make_sound())
print(bird.name, "makes sound", bird.make_sound())
