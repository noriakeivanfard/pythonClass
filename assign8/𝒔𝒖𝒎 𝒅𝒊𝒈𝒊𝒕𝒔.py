s = input("enter your sentence: ")
sum = 0
n = []
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in numbers: 
     for j in s:
      if str(i) == j:
         sum += i
      else:              
            n.append(j)
print(sum)
