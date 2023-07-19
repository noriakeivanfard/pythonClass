def gcd(first, second):
    first = int(input('enter first number: '))
    second = int(input('enter second number: '))
    if first > second:
           bmm = second
    elif second > first: 
           bmm = first
    while bmm > 1:
        if first % bmm == 0 and second % bmm == 0:
            print(bmm)
            break
        else:
            bmm -= 1
        if first % bmm == 0 and second % bmm == 0:
            return print(bmm)
        
print(gcd(2,5))
