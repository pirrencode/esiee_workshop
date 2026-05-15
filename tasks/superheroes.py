class Superhero:
    def __init__(self, name, powers, origin, friends, age, alignment):
        self.name = name
        self.powers = list(powers)
        self.origin = origin
        self.friends = friends
        self.age = age
        self.alignment = alignment  # New alignment parameter added
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
        if self.energy >= 50:
            self.add_power("Flight")
            self.energy -= 50
            print(f"{self.name} takes off into the sky")
        else:
            print(f"{self.name} is too tired to fly")

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

    # --- NEW POWERS ---
    def mind_reading(self):
        if self.energy >= 15:
            self.add_power("Mind Reading")
            self.energy -= 15
            print(f"{self.name} is now reading the room's thoughts")
            
    def time_travel(self):
        if self.energy >= 80:
            self.add_power("Time Travel")
            self.energy -= 80
            print(f"{self.name} has leaped through time")
        else:
            print(f"{self.name} doesn't have enough energy to time travel")


# Example usage
if __name__ == "__main__":
    print("--- Hero 1 ---")
    ironman = Superhero("IronMan", ["tech"], "Earth", "Pepper", 35, "Good")
    ironman.print_name()
    ironman.print_attributes()
    ironman.fly()
    
    print("\n--- Hero 2 ---")
    professor_x = Superhero("Professor X", ["Telepathy"], "Earth", "Magneto", 55, "Good")
    professor_x.print_name()
    professor_x.print_attributes()
    professor_x.mind_reading()
    
    print("\n--- Hero 3 ---")
    loki = Superhero("Loki", ["Illusion Magic"], "Asgard", "Thor (sometimes)", 1054, "Anti-Hero")
    loki.print_name()
    loki.print_attributes()
    loki.teleportation()
    loki.time_travel()
    
