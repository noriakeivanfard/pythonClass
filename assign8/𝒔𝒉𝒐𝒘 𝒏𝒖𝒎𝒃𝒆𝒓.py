n = int(input('enter number: '))
ask = input('one or two?')

if ask == 'one':
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

elif ask == 'two':
    for i in range(n, 0, -1):
        for j in range(1, i + 1): 
            print(j, end="")
        print()
