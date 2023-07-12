import random
number = int(input('enter number:'))
a = 0
b = 100
while True:
    input_number = random.randint(a,b)
    if input_number == number :
        print(f" your number:{input_number}", "is win!")
        break
    elif input_number > number:
        print(f" your number:{input_number}", "payintar")
        b = input_number
        input_number = random.randint(a,b)
    else: 
        input_number < number
        print(f" your number:{input_number}", "balatar")
        a = input_number
        input_number = random.randint(a,b)
