import math
def Equation(a , b , c ):
    a = float(input("enter number 1:"))
    b = float(input("enter number 2:"))
    c = float(input("enter number 3:"))
    num = (b ** 2-4*a*c)
    if num > 0:
        x1 = (-b + (math.sqrt(num))) / (2 * a)
        x2 = (-b - (math.sqrt(num))) / (2 * a)
        print(x1 , x2)
    elif num == 0 :
        x3 = (-b / (2 * a))
        print(x3)

print(Equation(1,2,3 ))
