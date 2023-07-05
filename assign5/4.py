op=int(input("""
Six operations:
1.Celsius to Kelvin '___' 2.Celsius to Fahrenheit '___' 3.Kelvin to Celsius '___' 4.Kelvin to Fahrenheit '___' 5.Fahrenheit to Celsius '___' 6.Fahrenheit to Kelvin
Which operation?"""))

number = float(input("enter number: "))

if op == 1:
    end = number + 273.15
    print(end)

elif op == 2:
    end = (number * 9 / 5) + 32
    print(end)

elif op == 3:
    end = number - 273.15
    print(end)

elif op == 4:
    end = (number - 273.15) * (9 / 5) + 32
    print(end)

elif op == 5:
    end = (number - 32) * (5 / 9)
    print(end)

elif op == 6:
    end = (number - 32) * (5 / 9) + 273.15
    print(end)
else :
            print("please try again")
  
