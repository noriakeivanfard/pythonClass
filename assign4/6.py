number = float(input("enter number: "))
if number < 0 :
    print('D')
else :
    if number % 2 == 0 and number > 4 :
     print('A')
    elif number % 2 == 0 and number < 4 :
     print('B')
    else:
     print('c')
