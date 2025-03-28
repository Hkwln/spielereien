#requirements: this programm gets a number and checks if this number is a prime number
import numpy as np

def Millerrabin(number):
    if number == 1:
        return True
    elif number % 2 != 0:
        numbers = []
        def createlist(number):
            temp = int(number -1)
            while temp % 2 ==0:
                numbers.append(int(temp))
                temp = temp/2
            
            numbers.append(int(temp))
            numbers.sort()
        createlist(number)

        #print(numbers)
        a = np.random.randint(1, 199)
        
        solution = []
        for k in numbers:

            b = pow(a, k, number)
            solution.append(b)
        #print(solution)
        prime = False
        counter = 0
        for i in range(len(solution)):
            if solution[i]== number-1:
                prime = True
            if solution[i] == 1:
                counter = counter +1
        #print (len(solution))
        #print (counter)
        if prime and counter>=1 or counter == len(solution):
            
            return True
        else:
             
            return False      
    elif number == 2:
        
        return True

    else:
        
        return False

def main():
    number = int(input("what prime number do you want to test?"))
    if Millerrabin(number) == True:
        print(" it is a prime number")
    else:
        print("it is not a prime number")
# if you uncomment the main() operation, you should be able to classify your number
#main()