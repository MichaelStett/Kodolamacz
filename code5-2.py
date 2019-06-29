import math
from abc import ABC, abstractmethod


class Wezel(ABC):
    def __init__(self, nazwa):
        self.__nazwa = nazwa

    def Wypisz(self):
        print(f"{self._Wezel__nazwa} ", end='')

    @abstractmethod
    def Wartosc(self):
        pass


class Liczba(Wezel):
    def __init__(self, a):
        super().__init__(__class__.__name__)
        self.__a = a

    def Wypisz(self):
        super().Wypisz()
        print(f"= {self.__a}")

    def Wartosc(self):
        return self.__a


class Dzialanie(Wezel):
    def __init__(self, a,  b, nazwa):
        super().__init__(nazwa)
        self.__a = a
        self.__b = b

    def Wypisz(self, dzialanie, wynik):
        super().Wypisz()
        print(
            f"{self._Dzialanie__a.Wartosc()}{dzialanie}{self._Dzialanie__b.Wartosc()} = {round(wynik, 2)}")

    @abstractmethod
    def Wartosc(self):
        pass


class Dodawanie(Dzialanie):
    def __init__(self, a,  b):
        super().__init__(a, b, __class__.__name__)

    def Wypisz(self):
        super().Wypisz("+", self.Wartosc())

    def Wartosc(self):
        return self._Dzialanie__a.Wartosc() + self._Dzialanie__b.Wartosc()


class Odejmowanie(Dzialanie):
    def __init__(self, a,  b):
        super().__init__(a, b, __class__.__name__)

    def Wypisz(self):
        super().Wypisz("-", self.Wartosc())

    def Wartosc(self):
        return self._Dzialanie__a.Wartosc() - self._Dzialanie__b.Wartosc()


class Mnozenie(Dzialanie):
    def __init__(self, a,  b):
        super().__init__(a, b, __class__.__name__)

    def Wypisz(self):
        super().Wypisz("*", self.Wartosc())

    def Wartosc(self):
        return self._Dzialanie__a.Wartosc() * self._Dzialanie__b.Wartosc()


class Dzielenie(Dzialanie):
    def __init__(self, a,  b):
        super().__init__(a, b, __class__.__name__)

    def Wypisz(self):
        super().Wypisz("/", self.Wartosc())

    def Wartosc(self):
        return self._Dzialanie__a.Wartosc() / self._Dzialanie__b.Wartosc()

class Silnia(Wezel):
    def __init__(self, a):
        super().__init__(__class__.__name__)
        self.__a = a

    def Wypisz(self):
        super().Wypisz()
        print(f"{self.__a.Wartosc()}! = {self.Wartosc()}", end='')

    def Wartosc(self):
        return math.factorial(self.__a.Wartosc())

if __name__ == "__main__":
    Liczba_5 = Liczba(5)
    Liczba_4m = Liczba(-4)
    Liczba_8 = Liczba(8)
    Liczba_0 = Liczba(0)
    Liczba_12 = Liczba(12)
    Liczba_3 = Liczba(3)

    Liczba_12.Wypisz()

    Mnozenie(Liczba_3, Liczba_4m).Wypisz()
    Dzielenie(Liczba_12, Liczba_5).Wypisz()
    Dodawanie(Liczba_8, Liczba_4m).Wypisz()
    Odejmowanie(Liczba_3, Liczba_8).Wypisz()

    Dodawanie(
        Mnozenie(Liczba_3, Liczba_4m), 
        Mnozenie(Liczba_12, Liczba_5)
        ).Wypisz()

    Dzielenie(
        Dodawanie(Liczba_3, Liczba_4m), 
        Odejmowanie(Liczba_12, Liczba_5)
        ).Wypisz()

    Silnia(Liczba_5).Wypisz()