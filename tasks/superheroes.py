"""Simple superhero utilities."""


class Superhero:
    def __init__(self, name, powers, origin, friends, age, alignement):
        self.name = name
        self.powers = list(powers)
        self.origin = origin
        self.friends = friends
        self.age = age
        self.energy = 100
        self.alignement = alignement

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

    def ultra_speed(self):
        if self.energy < 15
            return
        self.add_power("Ultra Speed")
        self.energy -= 15
        print(f"{self.name} reaches the speed of light")

    def liliput_size(self):
        if self.energy < 30:
            return
        self.add_power("Liliput Size")
        self.energy -= 30
        print(f"{self.name} becomes the size of a green pea")


# Example usage
if __name__ == "__main__":
    ironman = Superhero("IronMan", ["tech"], "Earth", "Pepper", 35, "Good")
    ironman.print_name()
    ironman.print_attributes()
    ironman.fly()

    miniman = Superhero("Miniman", [], "Venus", ["Michael Jackson", "Kim Jong Il"], 134, "Bad")
    miniman.print_name()
    miniman.print_attributes()
    miniman.liliput_size()

    flash = Superhero("Flash", [], "CEV31", ["Elon Musk", "Spongebob", "Miniman"], 9, "Bad")
    flash.print_name()
    flash.print_attributes()
    flash.ultra_speed()
