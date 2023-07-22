numbers = []
def number(n):
    n = int(input("enter a number: "))
    for i in range (1, 4):
        numbers.append(str(n * i))
    number = " ".join(numbers)
    number = number.replace(" ", "")
    return number
print(number(1))
