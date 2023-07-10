numbers1 = []

for i in range(10):
    
    nu1 = int(input("enter youre number: "))
    numbers1.append(nu1)


numbers2 = []  
c = 0  
while c < len(numbers1):
    a = numbers1[c] + 2    
    numbers2.append(a)
    c += 1

print(numbers1)
print(numbers2)
