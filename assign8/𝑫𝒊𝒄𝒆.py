import random
numbers = 0
num = 0
list_number = []
c = 0
while (numbers != 6): 
    list_number.append(numbers)
    numbers = random.randint(1, 6)
    c += 1
    if numbers == 6:
        print(f"round {c} is win")
        num += numbers
    print(f"round {c} is:", numbers)

