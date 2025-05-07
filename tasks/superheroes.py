# In this python program we will work on classess and objects

# TASK 1. Let's create a class -> superhero
# DEFINE A CLASS

# TASK 2. ADD POWER, ORIGIN AND FRIENDS ATTRIBUTES

class superhero :
  def __init__(self, name, power, origin, friends):
    self.name = name
    self.power = power
    self.origin = origin
    self.friends = friends
    self.age = age
  def printName(self):
    print(self.name)
  def printAttributes(self):
    print("Superhero attributes are: ")
    print(self.name)
    print(self.power)
    print(self.origin)
    print(self.friends)
    print(self.age)
    
# Ironman = superhero("IronMan")
SuperMan = superhero("SuperMan","flight", "plante X" , "SuperWoman",25)
Batman = superhero("Batman",["flight","super strong","brave","supercar"],"Earth","Catwoman",35)
Ironman.printName()
SuperMan.printAttributes()

# TASK 3. Add methods for use of 5 superpowers (minimum). Method must initialize a superpower

# TASK4. CREATE ACTIONS TO USE SUPERPOWERS
