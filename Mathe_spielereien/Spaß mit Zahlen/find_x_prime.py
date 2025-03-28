from Millerrabin import Millerrabin

def findnext(start, anzahl):
    i = 1
    prime = []
    if anzahl >0:
        if Millerrabin(start):
            prime.append(start)
            anzahl= anzahl-1
        while anzahl !=0:
            if (start+i) %2 != 0:
                if Millerrabin(start+i):
                    
                    prime.append(start+i)
                    anzahl = anzahl-1
            i = i+1
    return prime

def main():
    start = 80
    anzahl = 3
    prime = findnext(start, anzahl)
    print(prime)
main()

        