#Here i want to find for a given number the closest prime number
from Millerrabin import Millerrabin

def closestprime(number):
    if Millerrabin(number) == True:
        print(number)
    #here check the neares odd numbers if they are prime
    else:
        search = True
        i = 1
        while search:
            
            pclosest = number +i
            nclosest = number -i
            if pclosest %2 !=0:
                if Millerrabin(pclosest) == True:
                    print(pclosest)
                    search = False
            if nclosest %2 != 0:
                if Millerrabin(nclosest) == True:
                    print (nclosest)
                    search = False
            else:
                i = i+1

def main():
    number = int(input("give me a number you want to find the closest prime number"))
    closestprime(number)
main()