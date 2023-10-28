from math import *

def quad():
    if abs(a) > 0:
        if (b**2) < (4*a*c):
            print('Opps, your result is a Complex number!!!!')		

        elif (b**2) > (4*a*c):
            x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
            x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)

            print(f"x1 is {x1}")
            print(f"x2 is {x2}")
            print(f"So therefore the root are {x1} and {x2}")
        elif (b**2) == (4*a*c):
            x = (-b)/(2*a)
            print(f'Opps We have two Equal Root, x1 and x2 is = {x}')
    else:
        return None

a = int(input("Enter coefficient of x^2: "))
b = int(input("Enter coefficient of x: "))
c = int(input("Enter the constant: "))
quad()


