def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)
    
a = int(input("enter  first number: "))
b = int(input("enter second  number: "))
print("Result is:",GCD(a,b))
