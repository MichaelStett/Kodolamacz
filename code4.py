import math

class FunkcjaKwadratowa:
    def __init__(self, a, b, c): # konstruktor
        self.a = a
        self.b = b
        self.c = c

    def print(self):
        print(f"f(x) = {self.a}*x^2 + {self.b}*x + {self.c}.")        

    def wartoscDla(self, x):
        return self.a*x*x + self.b*x + self.c

    def Rozwiaz(self):
        self.print()
        if self.a == 0:
            if   self.b == 0 and self.c == 0:
                 print(f"Nieskonczenie wiele miejsc zerowych.")
            elif self.b != 0 and self.c == 0:                  
                 print(f"Miejsce zerowe to {0}.")              
            elif self.b == 0 and self.c != 0: 
                 print(f"Brak miejsc zerowych.")
            elif self.b != 0 and self.c != 0: 
                 print(f"Miejsce zerowe to {-(self.c) / self.b}.")
        else:
            delta = self.b**2 - 4 * self.a * self.c            
            print(f"Delta = {delta}, ", end="")

            if delta < 0: 
                print("brak rozwiązań.")
            elif delta >= 0: 
                delta = math.sqrt(delta)
                x1 = (-(self.b) + delta) / (2 * self.a)
                x2 = (-(self.b) - delta) / (2 * self.a)

                if x1 == x2:
                    print(f"jedno rozwiązanie: {x1}.")
                    # print(f"Sprawdzenie: {self.wartoscDla(x1)}")
                else:
                    print(f"dwa miejsca zerowe: {x1} oraz {x2}.")
                    # print(f"Sprawdzenie: {self.wartoscDla(x1)} oraz {self.wartoscDla(x2)}")


def main():
    #region FunkcjaKwadratowa 
    FunkcjaKwadratowa(1, 6, 5).Rozwiaz() # delta dodatnia ( 4 )
    FunkcjaKwadratowa(1, 0, 4).Rozwiaz() # delta ujemna ( -16 )
    FunkcjaKwadratowa(1,10,25).Rozwiaz() # delta zero ( 0 )
    FunkcjaKwadratowa(0, 7, 5).Rozwiaz() # a == 0
    FunkcjaKwadratowa(0, 1 ,0).Rozwiaz() # a == 0 and c == 0
    FunkcjaKwadratowa(0, 0, 1).Rozwiaz() # a == 0 and b == 0
    FunkcjaKwadratowa(0, 0 ,0).Rozwiaz() # a == 0 and b == 0 and c == 0
    #endregion

if __name__ == "__main__":
    main()