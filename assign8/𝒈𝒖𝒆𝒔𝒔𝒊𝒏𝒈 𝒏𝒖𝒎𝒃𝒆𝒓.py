import random
number = int(input('enter number:'))
c = 0
a = 0
b = 100
input_number = random.randint(a,b)
while True:
    if input_number == number :
             print(f" your number:{input_number}", "is win!")
             c += 1
             break
    elif input_number > number:
            print(f" your number:{input_number}", "payintar")
            num = input_number
            input_number = random.randint(a,b)
    else: 
        input_number < number
        print(f" your number:{input_number}", "balatar")
        num = input_number
        input_number = random.randint(a,b)

