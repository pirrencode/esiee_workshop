###### Task ######
#
# Create an Animal base class with a method make_sound()
# Subclasses: Dog, Cat, Bird with custom implementations of make_sound()
# Instantiate each and call make_sound()
##################

# BONUS: Add static method

@staticmethod
def createAnimal(animal, race):
    if animal == "Dog":
        return Dog(race)
    elif animal == "Cat":
        return Cat(race)
    elif animal == "Bird":
        return Bird(race)
    else:
        print("Sorry I dont know this animal")


class Animal:
    def __init__(self,race,sound):
        self.race = race
        self.sound = sound
    def make_sound(self):
        print(f"{self.race} says : {self.sound}")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Bark")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name, "PiouPiou")


dog1 = Dog("Oslo")
cat1 = Cat("Aziza")
bird1 = Bird("Coco")

dog2 = createAnimal("Dog", "Oslo")
bird2 = createAnimal("Bird", "Coco")

dog1.make_sound()
cat1.make_sound()
bird1.make_sound()

dog2.make_sound()
bird2.make_sound()