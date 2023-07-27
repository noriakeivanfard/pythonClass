a_1 = float(input("enter a_1 : "))
b_1 = float(input("enter b_1 : "))
a_2 = float(input("enter a_2 : "))
b_2 = float(input("enter b_2 : "))

op=int(input("""
1_sum
2_minus
which one?"""))
 
dict_number =  {"a_1": a_1, "b_1": b_1, "a_2": a_2, "b_2": b_2} 

if op == 1:
    def sum(dict_number):
     return f"{dict_number['a_1'] + dict_number['a_2']}, {dict_number['b_1'] + dict_number['b_2']}" + "i"
    print(sum(dict_number))
elif op == 2:
    def minus(dict_number):
     return f"{dict_number['a_1'] - dict_number['a_2']}, {dict_number['b_1'] - dict_number['b_2']}" + "i"
    print(minus(dict_number)) 
