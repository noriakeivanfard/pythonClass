import math
while True:
 print("1.- , 2.* , 3.+ , 4./ , 5.// , 6.% , 7.** ")
 print("8.log , 9.sin , 10.tan , 11.cos ,12.abs ")
 num1 = float(input("Enter number1 : "))
 num2 = float(input("Enter number2 : "))
 op = int(input("Enter a number1 and number2 for the operator from the list above: "))
 if op== 1 :
            print(num1 - num2)
 elif op == 2 :
      print(num1 * num2)
 elif op == 3 :
            print(num1 + num2)
 elif op == 4 :
            print(num1 / num2)
 elif op == 5 :
            print(num1 // num2)
 elif op == 6 :
            print(num1 % num2)
 elif op == 7 :
            print(num1 ** num2)
 elif op == 8 :
           print(math.log(num1))
 elif op == 9 :
            print(math._sin(num1))
 elif op == 10 :
            print(math.ten(num1))
 elif op == 11 :
            print(math.cos(num1))
 elif op == 12 :
            print(math.abs(num1))
 else :
            print("please try again")
 ask = input('do you want exit?:(yes or no)')
 if ask == 'yes':
    exit(0)

 else:
    ask == 'no'
