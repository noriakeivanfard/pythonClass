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
 
    def div(self):
     if (self.m_2['m'] != 0 or self.m_2["s"] != 0):
      answer_s = self.m_1["s"] * self.m_2['m']
      answer_m = self.m_1['m'] * self.m_2["s"]
      return answer_s , answer_m

op=int(input("""
1_sum
2_min
3_mul
4_div
which one?"""))

dct1  = {}
dct2 = {}  
    
for i in range(2):
    s = int(input("enter number_s: "))
    m = int(input("enter number_m: "))
    if i == 0:
        dct1  = {"s":s, "m":m}
    else:
        dct2 = {"s":s, "m":m}

def show(a,b):
    print("  "+str(a)+ "\n-----\n  "+ str(b))
 
d = deduction(dct1, dct2) 
if op == 1:
    a , b = d.sum()
    show(a,b)
elif op == 2:
    a , b = d.min()
    show(a,b)
elif op == 3:
    a , b = d.mul()
    show(a,b)
elif op == 4:
    a , b = d.div()
    show(a,b) 
