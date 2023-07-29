class time:
    def __init__(self,time1_dict,time2_dict):
    # Properties
     self.h1 = time1_dict
     self.h2 = time2_dict 
     
     self.m1 = time1_dict
     self.m2 = time2_dict 
     
     self.s1 = time1_dict
     self.s2 = time2_dict 
    
    # Methods
    def sum(self):
     h = self.h1["hour"] + self.h2["hour"]
     m = self.m1["minut"] + self.m2["minut"]
     s = self.s1["second"] + self.s2["second"]
     return h , m , s 
     
    def min(self):    
     h = self.h1["hour"] - self.h2["hour"]
     m = self.m1["minut"] - self.m2["minut"]
     s = self.s1["second"] - self.s2["second"]
     return h , m , s 

hour = int(input("enter hours: "))
minut = int(input("enter minuts: "))
second = int(input("enter seconds: "))
time1_dict = {"hour":hour,
              "minut":minut,
              "second":second}

hour = int(input("enter hours: "))
minut = int(input("enter minuts: "))
second = int(input("enter seconds: "))
time2_dict = {"hour":hour,
              "minut":minut,
              "second":second}

op=int(input("""
1_sum
2_min
which one?"""))

def show_time(h,m,s):
    print(f"{h}:{m}:{s}")  

t = time(time1_dict,time2_dict)  

if op == 1:
    h , m , s= t.sum()
    show_time(h,m,s)
elif op == 2:
    h , m , s= t.min()
    show_time(h,m,s) 
