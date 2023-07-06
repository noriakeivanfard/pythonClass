number = int(input("enter number:"))
m=number/7
if number % 7 == 0:
    print(f"{number} is multiple 7")
else:
    print(f"{number} is not multiple 7 ")
    number *= 7
    number += 7
    print(f"{number}Close to a multiple 7")
