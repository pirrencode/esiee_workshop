"""Simple superhero utilities."""


class Superhero:
    def __init__(self, name, powers, origin, friends, age, alignment):
        self.name = name
        self.powers = list(powers)
        self.origin = origin
        self.friends = friends
        self.age = age
        self.alignment = alignment
        self.energy = 100

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

    def time_travel(self):
        if self.energy >= 30:
            self.add_power("Time Travel")
            self.energy -= 30
            print(f"{self.name} travels through time")

    def heal(self):
        if self.energy >= 15:
            self.add_power("Healing")
            self.energy -= 15
            print(f"{self.name} heals rapidly")

# Example usage
if __name__ == "__main__":
    ironman = Superhero("IronMan", ["tech"], "Earth", "Pepper", 35)
    thor = Superhero("Thor", ["Lightning", "Strength"], "Asgard", ["Loki"], 1500, "Hero")
    loki = Superhero("Loki", ["Magic", "Illusion"], "Jotunheim", ["Thor"], 1050, "Anti-Hero")
    ironman.print_name()
    ironman.print_attributes()
    ironman.fly()

    
