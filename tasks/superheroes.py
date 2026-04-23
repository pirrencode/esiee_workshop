"""Simple superhero utilities."""


class Superhero:
    def __init__(self, name, powers, origin, friends, age, alignment):
        self.name = name
        self.powers = list(powers)
        self.origin = origin
        self.friends = friends
        self.age = age
        self.energy = 100
        self.alignment = alignment 

    def print_name(self):
        print(self.name)

    def print_attributes(self):
        print("Superhero attributes are:")
        print(self.name)
        print(self.powers)
        print(self.origin)
        print(self.friends)
        print(self.age)
        print(self.alignment) 

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
#New power
    def heal(self):
        self.add_power("Healing")
        self.energy += 30
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} heals and restores energy")

    def super_speed(self):
        if self.energy >= 15:
            self.add_power("Super Speed")
            self.energy -= 15
            print(f"{self.name} moves at incredible speed")

#New parameter
        def show_alignment(self):
        if self.alignment == 0:
            print("It is a good superhero")
        else:
            print("It is a bad superhero")


# Example usage
if __name__ == "__main__":
    ironman = Superhero("IronMan", ["tech"], "Earth", "Pepper", 35, 0)
    ironman.print_name()
    ironman.print_attributes()
    ironman.fly()
    ironman.show_alignment()

#New heros
    superman = Superhero("Superman", ["heal"], "New York", "Pepper", 35, 0)
    superman.print_name()
    superman.print_attributes()
    superman.fly()
    superman.show_alignment()

    loki = Superhero("Loki", ["super_speed"], "UK", "Nobody", 35, 1)
    loki.print_name()
    loki.print_attributes()
    loki.fly()
    loki.show_alignment()
