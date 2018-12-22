def main():    
    c = 't'
    while c == 't':
        print("Podaj w oddzielnych wierszach liczbę, operację matematyczną: +,-,*,/,%, a następnie kolejną liczbę: ")
        x = float(input())
        y = input()
        z = float(input())

        if y == '+':
            print("Twój wynik to: " + str(x + z))
        elif y == '-':
            print("Twój wynik to: " + str(x - z))
        elif y == '*':
            print("Twój wynik to: " + str(x * z))
        elif y == '/' and z != 0:            
            print("Twój wynik to: " + str(x / z))
        elif y == '%' and z != 0:
            print("Twój wynik to: " + str(x % z))
        else:
            print("nie dzieli sie przez zero!")            
        
        c = input("Kontynuowac? t/n ")
if __name__ == "__main__":
    main()