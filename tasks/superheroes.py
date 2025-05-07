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
    self.energy = 100
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
def fly(self):
  self.add_power("Flight")
  self.energy = energy - 50
  print(f"{self.name} "takes off into the sky")
  
def turn_invisible(self):
  if energy => 1:
    self.add_power("Invisibility")
    self.energy = energy - 1
    print(f"{self.name} "Becomes completely invisible")

  def super_strength(self):
    if energy => 10:  
      self.add_power("super strength")
      self.energy = energy - 10
      print(f"{self.name} "Become strong")

 def teleportation(self):
     if energy => 10:
      self.add_power("teleportation")
      self.energy = energy - 10
      print(f"{self.name} "instantly teleport")

def shoot_lasers(self):
    if energy => 20:
      self.add_power("shoot lasers")
      self.energy = energy - 20
      print(f"{self.name} "shoots lasers from eyes")
  
# TASK4. CREATE ACTIONS TO USE SUPERPOWERS
