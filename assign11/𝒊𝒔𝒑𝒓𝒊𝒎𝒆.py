number = int(input('enter your number: '))
active = True
while active:
    if number <= 1: 
        print('your number is not prime')
        break
    if number <= 3: 
        print('your number is prime')  
        break
    if number % 2 == 0 or number % 3 == 0: 
        print('your number is not prime')
        break
    i = 5
    while i * i <= number: 
        if number % i == 0 or number % (i + 2) == 0: 
            print('your number is not prime')
            break
        i = i + 6
    active = False
    print('your number is prime') 
