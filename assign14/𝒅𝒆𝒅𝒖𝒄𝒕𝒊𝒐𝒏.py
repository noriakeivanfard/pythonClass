def number(s,m):
    d = {"s": s, "m": m}
    return d

class deduction:
    def __init__(self, dict1 , dict2):
    # Properties
     self.m_1 = dict1
     self.m_2 = dict2
    # Methods
    def sum(self):
     answer_s = (self.m_1["s"] * self.m_2["m"]) + (self.m_2["s"] * self.m_1["m"])
     answer_m = self.m_1["m"] * self.m_2["m"]
     return answer_s , answer_m 
 
    def min(self):
     answer_s = (self.m_1["s"] * self.m_2["m"]) - (self.m_2["s"] * self.m_1["m"])
     answer_m = self.m_1["m"] * self.m_2["m"]
     return answer_s , answer_m
 
    def mul(self):
     answer_s = self.m_1["s"] * self.m_2["s"]
     answer_m = self.m_1['m'] * self.m_2['m']
     return answer_s , answer_m
 
    def Div(self):
     if (self.m_2['m'] != 0 or self.m_2["s"] != 0):
      answer_s = self.m_1["s"] * self.m_2['m']
      answer_m = self.m_1['m'] * self.m_2["s"]
      return answer_s , answer_m

op=int(input("""
1_sum
2_min
3_mul
4_Div
which one?"""))

dct1  = {}
dct2 = {}  
    
for i in range (1, 3):
    s = int(input(f"enter s{i}: "))
    m = int(input(f"enter m{i}: "))
    if i == 1:
        dct1  = number(s, m)
    else:
        dct2 = number(s, m) 
 
d = deduction(dct1, dct2)
if op == 1:
    a , b = d.sum()
    print(a, "\n-----\n", b)
elif op == 2:
    a , b = d.min()
    print(a, "\n-----\n", b)
elif op == 3:
    a , b = d.mul()
    print(a, "\n-----\n", b)
elif op == 4:
    try:
        a , b = d.Div()
        print(a, "\n-----\n", b)
    except:
        print(d.Div(dct1, dct2))  
