op=int(input("""
1_sum
2_minus
3_multiplication
4_Division
which one?"""))

for i in range(2):
    s = int(input("enter number_s: "))
    m = int(input("enter number_m: "))
    if i == 0:
        dct1  = {"s":s, "m":m}
    else:
        dct2 = {"s":s, "m":m}

def show(s,m):
    print("  "+str(s)+ "\n-----\n  "+ str(m))
    
if op == 1:
 def sum(m_1, m_2):
    answer_s = (m_1["s"] * m_2["m"]) + (m_2["s"] * m_1["m"])
    answer_m = m_1["m"] * m_2["m"]
    return answer_s , answer_m
 a , b = sum(dct1, dct2)
 show(a,b)
 
elif op == 2:
 def minus(m_1, m_2):
    answer_s = (m_1["s"] * m_2["m"]) - (m_2["s"] * m_1["m"])
    answer_m = m_1["m"] * m_2["m"]
    return answer_s , answer_m
 a , b = minus(dct1, dct2)
 show(a,b)
 
elif op == 3:
 def multiplication(m_1, m_2):
    answer_s = m_1["s"] * m_2["s"]
    answer_m = m_1['m'] * m_2['m']
    return answer_s , answer_m
 a , b = multiplication(dct1, dct2)
 show(a,b)

elif op == 4:
 def Division(m_1, m_2):
    if (m_2['m'] != 0 or m_2["s"] != 0):
     answer_s = m_1["s"] * m_2['m']
     answer_m = m_1['m'] * m_2["s"]
     return answer_s , answer_m
 a , b = Division(dct1, dct2)
 show(a,b)
else:
     print("equal to 0") 
