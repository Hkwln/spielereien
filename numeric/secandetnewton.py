#aim is to implement the secand method as well as the newton method:
import numpy



def f(x):
    return x**3 -2*x+2
#Input:
# the function and two intial point.
# As well as the number of iteration it should do
def secand(f, x0: int, x1: int, iterations: int = 5 ) -> float:
    for i in range(iterations):
        #calculating the secand of the two points
        ms= f(x1)-f(x0)/x1-x0
        x3 = (-ms*x1-f(x1))/ms
        if f(x1) == 0:
            print(x1)
        elif f(x0) == 0:
            print(x0)
        elif f(x3) == 0:
            print (x3)
        x3 = x0
    print (f"the current approximation of the zero point is {x0}")

#test:
secand(f, 0, 1)
def newton(f, x0:int, iterations:int = 5) -> float:
    # the formular is x_n+1 = x_n- (f(x_n))/f'(x_n)
    for i in range(iterations):
        x0=x0-numpy.divide(f(x0), numpy.diff(f(x0)))
        
    print (f"the current approximation of the zero point is {x0}")


#test
newton(f,0)







