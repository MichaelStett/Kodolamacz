def main():
    # print(sprytne(2,13))  
    # czyPalindrom()
    # x = input("Podaj napis1: ")
    # y = input("Podaj napis2: ")
    # print(czyAnagram(x, y))
    Lista = [1,2,3,4]
    print(moda(Lista))

def sprytne(x,y):
    if y == 1: 
        return x    
    elif y == 2:
        return x*x
    elif y == 3:
        return x*x*x
    elif y % 2 == 0:
        # parzyste
        return sprytne(x, int(y/2))*sprytne(x, int(y/2))
    else:
        #nieparzyste
        return 2*sprytne(x, int(y/2))*sprytne(x, int(y/2))

def czyPalindrom():
    napis = input("Podaj napis: ")
    napis = napis.lower()   
    flag = True
    for i in range(0, int(len(napis) / 2)):
        print(i)
        if napis[i] != napis[-(i + 1)]:
            flag = False
            break
    if flag == True:
        print(flag)
    else: 
        print(flag)

def czyAnagram(napis1, napis2):
    alfabet = { "a" : 0, "b" : 0, "c" : 0,
                "d" : 0, "e" : 0, "f" : 0,
                "g" : 0, "h" : 0, "i" : 0,
                "j" : 0, "k" : 0, "l" : 0,
                "m" : 0, "n" : 0, "o" : 0,
                "p" : 0, "q" : 0, "r" : 0,
                "s" : 0, "t" : 0, "u" : 0,
                "w" : 0, "v" : 0, "x" : 0,
                "y" : 0, "z" : 0,}

    if len(napis1) == len(napis2):
        for i in range(0,26):
            for j in range(0, len(napis1)):
                if chr(ord('a') + i) == napis1[j]:
                    alfabet[chr(ord('a') + i)] += 1
                if chr(ord('a') + i) == napis2[j]:
                    alfabet[chr(ord('a') + i)] -= 1        
        return all(value == 0 for value in alfabet.values())
    else: 
        return False

def moda(liczby):
    hold = {}

    for i in range(0, len(liczby)):
        if liczby[i] in hold:
            hold[liczby[i]] =+ 1
        else:
            hold[liczby[i]] = 0
    
    return max(k for k, v in hold.items() if v != 0)

if __name__ == "__main__":
    main()