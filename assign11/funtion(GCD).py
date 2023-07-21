def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)
    
a = int(input("enter number first: "))
b = int(input("enter number second: "))
print("Result is:",GCD(a,b))
