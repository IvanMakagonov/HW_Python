from abc import ABC, abstractmethod

class Kostum():
    perem = 0

    def __init__(self, a):
        self.a = a

    @property
    @abstractmethod
    def sist(self):
        pass

    def __str__(self):
        pera = Kostum.perem
        Kostum.perem = 0
        return f"{pera}"

    def __add__(self, other):
        Kostum.perem += self.sist + other.sist
        return Suit(0)

class Palto(Kostum):
    @property
    def sist(self):
        return round(2 * self.a + 0.3)

class Suit(Kostum):
    @property
    def sist(self):
        return round(self.a / 6.5 + 0.5)

p = Palto(20)
s = Suit(150)

print(type(p), type(s))
print(p + p + s)