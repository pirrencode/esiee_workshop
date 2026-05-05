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
        print(f"Name: {self.name}")
        print(f"Powers: {self.powers}")
        print(f"Origin: {self.origin}")
        print(f"Friends: {self.friends}")
        print(f"Age: {self.age}")
        print(f"Alignment: {self.alignment}")
        print(f"Energy: {self.energy}")

    def add_power(self, power):
        if power not in self.powers:
            self.powers.append(power)

    def fly(self):
        if self.energy >= 50:
            self.add_power("Flight")
            self.energy -= 50
            print(f"{self.name} takes off into the sky")
        else:
            print(f"{self.name} does not have enough energy to fly")

    def turn_invisible(self):
        if self.energy >= 1:
            self.add_power("Invisibility")
            self.energy -= 1
            print(f"{self.name} becomes completely invisible")
        else:
            print(f"{self.name} does not have enough energy to turn invisible")

    def super_strength(self):
        if self.energy >= 10:
            self.add_power("Super Strength")
            self.energy -= 10
            print(f"{self.name} becomes strong")
        else:
            print(f"{self.name} does not have enough energy for super strength")

    def teleportation(self):
        if self.energy >= 10:
            self.add_power("Teleportation")
            self.energy -= 10
            print(f"{self.name} instantly teleports")
        else:
            print(f"{self.name} does not have enough energy to teleport")

    def shoot_lasers(self):
        if self.energy >= 20:
            self.add_power("Shoot Lasers")
            self.energy -= 20
            print(f"{self.name} shoots lasers from eyes")
        else:
            print(f"{self.name} does not have enough energy to shoot lasers")

    def heal(self):
        if self.energy >= 15:
            self.add_power("Healing")
            self.energy -= 15
            print(f"{self.name} uses healing powers")
        else:
            print(f"{self.name} does not have enough energy to heal")

    def create_force_field(self):
        if self.energy >= 25:
            self.add_power("Force Field")
            self.energy -= 25
            print(f"{self.name} creates a powerful force field")
        else:
            print(f"{self.name} does not have enough energy to create a force field")


# Example usage
if __name__ == "__main__":
    ironman = Superhero("IronMan", ["Tech"], "Earth", ["Pepper"], 35, "Hero")
    spiderman = Superhero("SpiderMan", ["Wall Crawling", "Spider Sense"], "Earth", ["Ned", "MJ"], 18, "Hero")
    scarlet_witch = Superhero("Scarlet Witch", ["Chaos Magic", "Telekinesis"], "Earth", ["Vision"], 29, "Anti-Hero")

    ironman.print_name()
    ironman.print_attributes()
    ironman.fly()
    ironman.create_force_field()

    print()

    spiderman.print_name()
    spiderman.print_attributes()
    spiderman.super_strength()
    spiderman.turn_invisible()

    print()

    scarlet_witch.print_name()
    scarlet_witch.print_attributes()
    scarlet_witch.teleportation()
    scarlet_witch.heal()
