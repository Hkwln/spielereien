#requirements: this programm gets a number and checks if this number is a prime number
#current errors: if the array solutions has only 1 in it it doesn't recognice the number as prime
#sometimes it doesn't give any output
import numpy as np

number = int(input("what prime number do you want to test?"))
def Millerrabin(number):
    if number % 2 != 0:
        #go on with the algorithm
        numbers = []
        #teile die numer solange durch 2 bis man eine ungerade zahl hat am ende, dann nimmt man eine zufällige zahl und nimmt a^zahlenbis ungerade zahl
        # jetzt muss mod number irgendwann -1 und dann nurnoch 1en kommen, oder direkt am anfang einsen
        
        def createlist(number):
            temp = int(number -1)
            while temp % 2 ==0:
                numbers.append(int(temp))
                temp = temp/2
            
            numbers.append(int(temp))
            numbers.sort()
        createlist(number)

        print(numbers)
        a = np.random.randint(1, 199)
        
        solution = []
        for k in numbers:

            b = pow(a, k, number)
            solution.append(b)
        print(solution)
        #now check the numbers in the array if there is a ...-1 1... anywhere
        for i in range(len(solution)-1):
            if solution[i]== number-1 or solution[i]== 1:
                #check if the following numbers are equal to 1
                for i in range(solution.index(number-1) +1, len(solution)):
                    if solution[i]!= 1:
                        print("this is not a prime number")
                        return False
                    print("this is a prime number")
                    return True
    elif number == 2:
        print("2 is a prime number")
        return True
    else:
        print("your number is not a prime number")
        return False

Millerrabin(number)