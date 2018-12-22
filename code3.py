def main():
    # print(sprytne(2,13))  
    czyPalindrom()

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

if __name__ == "__main__":
    main()