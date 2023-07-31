def check(h, m, s):
    while not(0 <= s <= 60 and 0 <= m <= 60):
        if s >= 60:
            s -= 60
            m += 1
        if s < 0:
            m -= 1
            s += 60
        if m >= 60:
            m -= 60
            h += 1
        if m < 0:
            h -= 1
            m += 60
    return h,m,s

class Time:
    def __init__(self, h1, h2, m1, m2, s1, s2):
        self.h1 = h1
        self.h2 = h2
        self.m1 = m1
        self.m2 = m2
        self.s1 = s1
        self.s2 = s2

    def sum(self):
        h, m, s = self.h1 + self.h2, self.m1 + self.m2, self.s1 + self.s2
        h, m, s = check(h, m, s)
        return h,m,s
    
    def min(self):
        h, m, s = self.h1 - self.h2, self.m1 - self.m2, self.s1 - self.s2
        h, m, s = check(h, m, s)
        return h,m,s

    def show(self, h, m, s):
        print(f"{h}:{m}:{s}")

time1 = input("enter time1:like(00:00:00) ")
time2 = input("enter time2:like(00:00:00) ")
op = int(input("""
1_sum
2_min
which one?"""))
            
t1 = time1.split(":")
t2 = time2.split(":")

time = Time(int(t1[0]), 
            int(t2[0]), 
            int(t1[1]), 
            int(t2[1]), 
            int(t1[2]), 
            int(t2[2])) 

if op == 1:
    h, m, s = time.sum()
    time.show(h, m, s)
elif op == 2:
    h, m, s = time.min()
    time.show(h, m, s) 
