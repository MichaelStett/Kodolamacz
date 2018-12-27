import math

class FunkcjaKwadratowa:
    def __init__(self, a, b, c): # konstruktor
        self.a = a
        self.b = b
        self.c = c
    def Rozwiaz(self):
        print(f"f(x) = {self.a}*x^2 + {self.b}*x + {self.c}.")        
        if self.a == 0:
            if   self.b == 0 and self.c == 0:
                 print(f"Nieskonczenie wiele miejsc zerowych.")
            elif self.b != 0 and self.c == 0:                  
                 print(f"Miejsce zerowe to {0}.")              
            elif self.b == 0 and self.c != 0: 
                 print(f"Brak miejsc zerowych.")
            elif self.b != 0 and self.c != 0: 
                 print(f"Miejsce zerowe to {self.b / self.c}.")
        else:
            x1 = 0
            x2 = 0
            delta = self.b*self.b - 4 * self.a * self.c            
            print(f"Delta = {delta}, ", end="")

            if delta < 0: 
                print("brak rozwiązań.")
            elif delta >= 0: 
                delta = math.sqrt(delta)
                x1 = (-(self.b) + delta) / (2 * self.a)
                x2 = (-(self.b) - delta) / (2 * self.a)

                if x1 == x2:
                    print(f"jedno rozwiązanie: {x1}.")
                else:
                    print(f"dwa miejsca zerowe: {x1} oraz {x2}.") 
                   

def main():
    f1 = FunkcjaKwadratowa(1, 6, 5) # delta dodatnia ( 4 )
    f1.Rozwiaz()

    f1 = FunkcjaKwadratowa(1, 0, 4) # delta ujemna ( -16 )
    f1.Rozwiaz()

    f1 = FunkcjaKwadratowa(1, 10, 25) # delta ujemna ( 0 )
    f1.Rozwiaz()

    f1 = FunkcjaKwadratowa(0, 7, 5) # a == 0
    f1.Rozwiaz()

    f1 = FunkcjaKwadratowa(0, 1 ,0) # a == 0 and c == 0
    f1.Rozwiaz()

    f1 = FunkcjaKwadratowa(0, 0, 1) # a == 0 and b == 0
    f1.Rozwiaz()

    f1 = FunkcjaKwadratowa(0, 0 ,0) # a == 0 and b == 0 and c == 0
    f1.Rozwiaz()

if __name__ == "__main__":
    main()