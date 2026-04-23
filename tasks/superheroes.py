"""Simple superhero utilities."""


class Superhero:
    def __init__(self, name, powers, origin, friends, age, role):
        self.name = name
        self.powers = list(powers)
        self.origin = origin
        self.friends = friends
        self.age = age
        self.energy = 100
        self.role = role

    def print_name(self):
        print(self.name)

    def print_attributes(self):
        print("Superhero attributes are:")
        print(self.name)
        print(self.powers)
        print(self.origin)
        print(self.friends)
        print(self.age)
        print(self.role)

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

    def dance(self):
        if self.energy >= 50:
            self.add_power("Dance on you")
            self.energy -= 50
            print(f"{self.name} Leg Danceeeeee")

    def mock(self):
        if self.energy >= 100:
            self.add_power("Mock")
            self.energy -= 100
            print(f"{self.name} mock his opponent")
        

# Example usage
if __name__ == "__main__":
    ironman = Superhero("IronMan", ["tech"], "Earth", "Pepper", 35, "Leader")
    batman = Superhero("Batman", ["intelligence"], "Gotham", "Robin", 40, "Detective")
    ironman.print_name()
    ironman.print_attributes()

    batman.print_name()
    batman.print_attributes()

    ironman.fly()
    ironman.shoot_lasers()
    ironman.teleportation()

    batman.turn_invisible()
    batman.super_strength()
    batman.dance()
    batman.mock()
    
