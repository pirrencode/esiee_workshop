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
        if self.energy >= 80:
            self.add_power("Time Travel")
            self.energy -= 80
            print(f"{self.name} travels through time")

    def mind_control(self):
        if self.energy >= 30:
            self.add_power("Mind Control")
            self.energy -= 30
            print(f"{self.name} controls minds")

if __name__ == "__main__":
    ironman = Superhero("IronMan", ["tech"], "Earth", "Pepper", 35, "good")
    thanos = Superhero("Thanos", ["strength"], "Titan", "None", 1000, "bad")
    spiderman = Superhero("Spider-Man", ["web"], "Earth", "Ned", 18, "good")

    ironman.print_attributes()
    thanos.time_travel()
    spiderman.mind_control()
