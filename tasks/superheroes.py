"""Simple superhero utilities."""


class Superhero:
    def __init__(self, name, powers, origin, friends, age, alignment):
        self.name = name
        self.powers = list(powers)
        self.origin = origin
        self.friends = friends
        self.age = age
        self.alignment = alignment  # "good" or "evil"
        self.energy = 100

    def print_name(self):
        print(self.name)

    def print_attributes(self):
        print("Superhero attributes are:")
        print("Name:", self.name)
        print("Powers:", self.powers)
        print("Origin:", self.origin)
        print("Friends:", self.friends)
        print("Age:", self.age)
        print("Alignment:", self.alignment)
        print("Energy:", self.energy)

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
            print(f"{self.name} does not have enough energy")

    def super_strength(self):
        if self.energy >= 10:
            self.add_power("Super Strength")
            self.energy -= 10
            print(f"{self.name} becomes strong")
        else:
            print(f"{self.name} does not have enough energy")

    def teleportation(self):
        if self.energy >= 10:
            self.add_power("Teleportation")
            self.energy -= 10
            print(f"{self.name} instantly teleports")
        else:
            print(f"{self.name} does not have enough energy")

    def shoot_lasers(self):
        if self.energy >= 20:
            self.add_power("Shoot Lasers")
            self.energy -= 20
            print(f"{self.name} shoots lasers from eyes")
        else:
            print(f"{self.name} does not have enough energy")

    def heal(self):
        if self.energy >= 15:
            self.add_power("Healing")
            self.energy -= 15
            print(f"{self.name} uses healing powers")
        else:
            print(f"{self.name} does not have enough energy")

    def control_thunder(self):
        if self.energy >= 25:
            self.add_power("Thunder Control")
            self.energy -= 25
            print(f"{self.name} summons thunder and lightning")
        else:
            print(f"{self.name} does not have enough energy")


# Example usage
if __name__ == "__main__":
    ironman = Superhero("IronMan", ["Tech"], "Earth", "Pepper", 35, "good")
    thor = Superhero("Thor", ["Hammer", "Strength"], "Asgard", "Loki", 1500, "good")
    loki = Superhero("Loki", ["Magic", "Illusion"], "Asgard", "Thor", 1050, "evil")

    ironman.print_name()
    ironman.print_attributes()
    ironman.fly()
    print()

    thor.print_name()
    thor.print_attributes()
    thor.control_thunder()
    thor.fly()
    print()

    loki.print_name()
    loki.print_attributes()
    loki.turn_invisible()
    loki.teleportation()

    
