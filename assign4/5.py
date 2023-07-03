weight = float(input('enter weight(KG): '))
height = float(input('enter height(M): '))
BMI = (height * height) / weight
print(BMI)
if BMI < 18.5:
    print('thin')
elif 18.5 < BMI < 24.9:
    print('normal')
elif 25.0 < BMI < 29.9:
    print('border of fat')
elif 30 < BMI < 34.9:
    print('fat')
else:
    print('very fat')
