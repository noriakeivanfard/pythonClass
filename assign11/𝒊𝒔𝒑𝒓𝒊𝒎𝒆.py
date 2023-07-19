def isprime(number):
    n = 0
    for i in range(1, number+1):
        if number%i == 0:
            n+=1
    if n==2:
        print('your number is prime')
    else:
        print('your number is not prime')
        
number = int(input("please enter your number :"))
print(isprime(number))
