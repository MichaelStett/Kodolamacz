import math
from abc import ABC, abstractmethod


class Figura(ABC):
    def __init__(self, nazwa):
        self.nazwa = nazwa

    @abstractmethod
    def Pole(self):
        pass

    @abstractmethod
    def Obwod(self):
        pass

    @abstractmethod
    def Wypisz(self):
        print(f"{self.nazwa}", end='')
        pass


class Kolo(Figura):
    def __init__(self, r, nazwa):
        super().__init__(nazwa)
        self.r = r

    def Pole(self):
        return (int)(math.pi*self.r) ^ 2

    def Obwod(self):
        return round(2*math.pi*self.r, 2)

    def Wypisz(self):
        super().Wypisz()
        print(f" R: {self.r}, Pole: {self.Pole()}, Obwod: {self.Obwod()}")


class Prostokat(Figura):
    def __init__(self, a, b, nazwa):
        super().__init__(nazwa)
        self.a = a
        self.b = b

    def Pole(self):
        return self.a * self.b

    def Obwod(self):
        return 2*self.a + 2*self.b

    def Wypisz(self):
        super().Wypisz()
        print(
            f" Boki: {self.a} {self.b}, Pole: {self.Pole()}, Obwod: {self.Obwod()}")


class Kwadrat(Prostokat):
    def __init__(self, a, nazwa):
        super(Kwadrat, self).__init__(a, a, nazwa)


class Trojkat(Figura):
    def __init__(self, a, b, c, nazwa):
        super().__init__(nazwa)
        self.a = a
        self.b = c
        self.c = c

    @staticmethod
    def CheckABC(a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            return 0
        else:
            return 1

    def Pole(self):
        p = self.Obwod() / 2
        wyn = math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
        return round(wyn, 2)

    def Obwod(self):
        return self.a + self.b + self.c

    def Wypisz(self):
        super().Wypisz()
        print(
            f" Boki: {self.a} {self.b} {self.c}, Pole: {self.Pole()}, Obwod: {self.Obwod()}")


if __name__ == "__main__":
    kolo = Kolo(5, "Kolo")
    kwadrat = Kwadrat(10, "Kwadrat")
    prostokat = Prostokat(5, 10, "Prostokat")
    trojkat = Trojkat(4, 5, 6, "Trojkat")

    figury = [kolo, kwadrat, prostokat, trojkat]

    for figura in figury:
        figura.Obwod()
        figura.Pole()
        figura.Wypisz()
