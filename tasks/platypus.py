"""Simple multi-level inheritance example with a Platypus class."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Animal(ABC):
    """Base class representing generic animals."""

    def __init__(self, name: str) -> None:
        self.name = name

    def describe(self) -> str:
        """Return a short description of the animal."""
        return f"{self.name} is an animal"

    @abstractmethod
    def make_sound(self) -> str:
        """Return the sound made by the animal."""
        raise NotImplementedError


class Mammal(Animal):
    """Mammal extends :class:`Animal` with mammal-specific features."""

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.warm_blooded = True

    def feed_milk(self) -> str:
        """Return a description of nursing the young."""
        return f"{self.name} nurses its young"


class EggLayer(ABC):
    """Mixin for animals that lay eggs."""

    @abstractmethod
    def lay_eggs(self) -> str:
        """Return a string describing egg-laying."""
        raise NotImplementedError


class Platypus(Mammal, EggLayer):
    """Platypus is a mammal that also lays eggs."""

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.can_swim = True
        self.has_bill = True

    def make_sound(self) -> str:
        """Return the typical sound of a platypus."""
        return f"{self.name} growls softly"

    def lay_eggs(self) -> str:
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
