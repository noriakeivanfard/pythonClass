number = int(input("enter your number:"))
a = 0

for i in range(1,number):
    if number % i == 0:
        a += i
    
if a != number:
	print("no")
else:
	print("yes")
