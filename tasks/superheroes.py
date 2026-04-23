"""Simple superhero utilities."""


class Superhero:
    def __init__(self, name, powers, origin, friends, age, alignment):
        self.name = name
        self.powers = list(powers)
        self.origin = origin
        self.friends = friends
        self.age = age
        self.energy = 100
        self.alignment = [alignment] 

    def print_name(self):
        print(self.name)

    def print_attributes(self):
        print("Superhero attributes are:")
        print(self.name)
        print(self.powers)
        print(self.origin)
        print(self.friends)
        print(self.age)
        print(f"Alignment: {self.alignment}")

    def add_alignment(self, alignment):
        if alignment not in self.alignment:
            self.alignment.append(alignment)

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
    def super_speed(self):
         if self.energy >= 5:
            self.add_power("Super Speed")
            self.energy -= 5
            print(f"{self.name} moves at incredible speed")

    def shield(self):
         if self.energy >= 15:
            self.add_power("Shield")
            self.energy -= 15
            print(f"{self.name} creates a protective shield")
         else:
            print(f"{self.name} is too tired!")




# Example usage
if __name__ == "__main__":
    ironman = Superhero("IronMan", ["tech"], "Earth", "Pepper", 35, "good")
    ironman.print_name()
    ironman.print_attributes()
    ironman.fly()
    ladybug = Superhero("LadyBug", ["speed"], "earth", "doggy", 750, "good")
    Bloom = Superhero("Bloom", ["fire"], "sun", "rabbit", 800, "leader")
