def gcd(first,second):
    first = int(input('enter first number: '))
    second = int(input('enter second number: '))
    if first > second:
        kmm = first
    elif second > first:
        kmm = second
        
    while kmm > 1:
        if kmm % first == 0 and kmm % second == 0:
            print(kmm)
            break
        else:
             kmm += 1
        if kmm % first == 0 and kmm % second == 0:
             return print(kmm)
print(gcd(2,5))
