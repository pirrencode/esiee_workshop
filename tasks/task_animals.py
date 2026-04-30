###### Task ######
#
# Create an Animal base class with a method make_sound()
# Subclasses: Dog, Cat, Bird with custom implementations of make_sound()
# Instantiate each and call make_sound()
##################

# Base class
class Animal:
    def make_sound(self):
        print("Some generic animal sound")

# Subclasses
class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Bird(Animal):
    def make_sound(self):
        print("Chirp")

# Instantiate and call methods
dog = Dog()
cat = Cat()
bird = Bird()

dog.make_sound()
cat.make_sound()
bird.make_sound()
