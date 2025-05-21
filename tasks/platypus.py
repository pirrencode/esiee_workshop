"""Simple multi-level inheritance example with a Platypus class."""


class Animal:
    """Base class representing generic animals."""

    def __init__(self, name: str) -> None:
        self.name = name

    def describe(self) -> str:
        """Return a short description of the animal."""
        return f"{self.name} is an animal"


class Mammal(Animal):
    """Mammal extends :class:`Animal` with mammal-specific features."""

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.warm_blooded = True

    def feed_milk(self) -> str:
        """Return a description of nursing the young."""
        return f"{self.name} nurses its young"


class Platypus(Mammal):
    """Platypus is a mammal that also lays eggs."""

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.can_swim = True
        self.has_bill = True

    def lay_eggs(self) -> str:
        """Return a string describing egg-laying."""
        return f"{self.name} lays eggs"

    def swim(self) -> str:
        """Return a string describing swimming."""
        return f"{self.name} paddles through the water"


if __name__ == "__main__":
    perry = Platypus("Perry")
    print(perry.describe())
    print(perry.feed_milk())
    print(perry.lay_eggs())
    print(perry.swim())
