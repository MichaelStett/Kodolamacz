def main():
    print(sprytne(2,13))

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

if __name__ == "__main__":
    main()