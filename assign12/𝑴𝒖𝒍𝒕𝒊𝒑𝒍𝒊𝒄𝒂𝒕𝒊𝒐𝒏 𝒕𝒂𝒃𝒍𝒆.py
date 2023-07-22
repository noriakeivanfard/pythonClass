def Multiplication_table(x,y):
    for i in range(1,x + 1):
        for j in range(1,y + 1):
            print(i * j,end = ' ')
        print()
x = int(input("enter x: "))
y = int(input("enter y: "))


Multiplication_table(x,y)
