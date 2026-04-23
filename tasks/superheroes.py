"""Simple superhero utilities."""

class Alignment:
    """Base class to define if a hero is Good, Evil, or Neutral."""
    def __init__(self, alignment="Good"):
        self.alignment = alignment
class Superhero(Alignment):
    def __init__(self, name, powers, origin, friends, age, alignment="Good"):
        # Initialisation de la classe parente Alignment
        super().__init__(alignment)
        self.name = name
        self.powers = list(powers)
        self.origin = origin
        self.friends = friends
        self.age = age
        self.energy = 100

class Superhero:
    def __init__(self, name, powers, origin, friends, age):
        self.name = name
        self.powers = list(powers)
        self.origin = origin
        self.friends = friends
        self.age = age
        self.energy = 100

    def print_name(self):
        
        print(f"Hero Name: {self.name} ({self.alignment})")

      def print_attributes(self):
        print(f"\n--- {self.name} Attributes ---")
        print(f"Alignment: {self.alignment}")
        print(f"Powers: {self.powers}")
        print(f"Origin: {self.origin}")
        print(f"Friends: {self.friends}")
        print(f"Age: {self.age}")
        print(f"Energy: {self.energy}")

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

    
     # --- New Powers ---
    def time_travel(self):
        """New Power 1: Time Travel"""
        if self.energy >= 80:
            self.add_power("Time Travel")
            self.energy -= 80
            print(f"{self.name} ripples through the fabric of time!")
        else:
            print(f"{self.name} is too tired to warp time.")

    def telepathy(self):
        """New Power 2: Telepathy"""
        if self.energy >= 15:
            self.add_power("Telepathy")
            self.energy -= 15
            print(f"{self.name} is reading minds...")



# Example usage
if __name__ == "__main__":
    ironman = Superhero("IronMan", ["tech"], "Earth", "Pepper", 35)
    ironman.print_name()
    ironman.print_attributes()
    ironman.fly()
        # 3) Adding 2 more superheroes
    spiderman = Superhero("Spider-Man", ["webs", "climbing"], "NYC", "Ned", 18, "Good")
    thanos = Superhero("Thanos", ["strength"], "Titan", "None", 1000, "Evil")
    # Testing new features
    spiderman.print_name()
    spiderman.telepathy()
    
    thanos.print_attributes()
    thanos.time_travel()
    thanos.print_attributes()



