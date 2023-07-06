number = int(input("Enter a number: "))
if number % 7 == 0:
    print("Yes")
else:
    largest_multiple_of_seven = 7 * (number // 7 + 1)
    print("largest multiple of seven ", largest_multiple_of_seven)
