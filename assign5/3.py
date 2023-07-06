number = int(input("Enter a number: "))

number_even = str(number)
number_odd = str(number)

even_count = number_even.count('0') + number_even.count('2') + number_even.count('4') + number_even.count('6') + number_even.count('8')  
odd_count = number_odd.count('1') + number_odd.count('3') + number_odd.count('5') + number_odd.count('7') + number_odd.count('9')

if odd_count > even_count:
    print("odd")
elif even_count > odd_count:
    print("even")
else:          
    print("equal")
