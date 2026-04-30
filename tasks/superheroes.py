"""Simple superhero utilities."""


class Superhero:
    def __init__(self, name, powers, origin, friends, age):
        self.name = name
        self.powers = list(powers)
        self.origin = origin
        self.friends = friends
        self.age = age
        self.energy = 100
        self.good_guy = True

    def print_name(self):
        print(self.name)

    def print_attributes(self):
        print("Superhero attributes are:")
        print(self.name)
        print(self.powers)
        print(self.origin)
        print(self.friends)
        print(self.age)

    def add_power(self, power):
        if power not in self.powers:
            self.powers.append(power)

    def fly(self):
        self.add_power("Flight")
        self.energy -= 50
        print(f"{self.name} takes off into the sky")

    def turn_invisible(self):
        if self.energy >= 1:
            self.add_power("Invisibility")
            self.energy -= 1
            print(f"{self.name} becomes completely invisible")

    def super_strength(self):
        if self.energy >= 10:
            self.add_power("Super Strength")
            self.energy -= 10
            print(f"{self.name} becomes strong")

    def teleportation(self):
        if self.energy >= 10:
            self.add_power("Teleportation")
            self.energy -= 10
            print(f"{self.name} instantly teleports")

    def shoot_lasers(self):
        if self.energy >= 20:
            self.add_power("Shoot Lasers")
            self.energy -= 20
            print(f"{self.name} shoots lasers from eyes")
            
    def heal(self):
        if self.energy >= 10:
            self.add_power("Heal")
            self.energy -= 30
            print(f"{self.name} instantly heal a hurt")
            
    def magnet(self):
        if self.energy >= 10:
            self.add_power("Magnet")
            self.energy -= 20
            print(f"{self.name} Magnetize metal objects")
            
    def super_speed(self):
        if self.energy >= 10:
            self.add_power("Super Speed")
            self.energy -= 20
            print(f"{self.name} runs at super speed")


# Example usage
if __name__ == "__main__":
    ironman = Superhero("IronMan", ["tech"], "Earth", "Pepper", 35, good_guy=True)
    magneto = Superhero("Magneto", ["magnetism"], "Earth", "Mystique", 60 , good_guy=False)
    quicksilver = Superhero("Quicksilver", ["super speed"], "Earth", "Scarlet Witch", 30 , good_guy=True)
    invisible_woman = Superhero("Invisible", ["invisibility"], "Earth", "Mr. Fantastic", 28 , good_guy=True)
    ironman.print_name()
    ironman.print_attributes()
    ironman.fly()
    ironman.shoot_lasers()
    magneto.print_name()
    magneto.print_attributes()
    magneto.magnet()
    magneto.fly()
    quicksilver.print_name()
    quicksilver.print_attributes()
    quicksilver.super_speed()
    quicksilver.heal()
    invisible_woman.print_name()
    invisible_woman.print_attributes()
    invisible_woman.turn_invisible()
