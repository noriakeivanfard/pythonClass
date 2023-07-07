numbers = []
nu1 = float(input("enter youre number: "))
nu2 = float(input("enter youre number: "))
nu3 = float(input("enter youre number: "))
nu4 = float(input("enter youre number: "))
nu5 = float(input("enter youre number "))

numbers.append(nu1)
numbers.append(nu2)
numbers.append(nu3)
numbers.append(nu4)
numbers.append(nu5)

a = sorted(numbers)
print(a)

b = sorted(numbers, reverse=True)
print(b)

