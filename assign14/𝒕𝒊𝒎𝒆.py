class time:
    def __init__(self,h1,h2,m1,m2,s1,s2):
    # Properties
        self.hour_s = h1 + h2
        self.minut_s = m1 + m2
        self.second_s = s1 + s2
        self.hour_m = h1 - h2
        self.minut_m = m1 - m2
        self.second_m = s1 - s2
        self.op = op
    # Methods
    def sum(self):
        while not(0 <= self.second_s <= 60 and 0 <= self.minut_s <= 60):
            if self.second_s >= 60:
                self.second_s -= ((self.second_s // 60) * 60)
                self.minut_s += (self.second_s // 60)
            if self.minut_s >= 60:
                self.minut_s -= ((self.minut_s // 60) * 60)
                self.hour_s += (self.minut_s // 60)
 
    def min(self):
            while not(0 <= self.second_m <= 60 and 0 <= self.minut_m <= 60):
                if self.second_m < 0:
                    self.minut_m -= 1
                    self.second_m += 60
                    if self.minut_m < 0:
                        self.hour_m -= 1
                        self.minut_m += 60

def show_time(h,m,s):
    print(f"{h}:{m}:{s}")

time1 = input("enter time1: ")
time2 = input("enter time2: ")
op=int(input("""
1_sum
2_min
which one?"""))
time1 = time1.split(":")
time2 = time2.split(":")
for i in time1:
 time1 = [eval(i)]
for i in time2:
 time2 = [eval(i)]
t = time(time1[0], time1[1], time1[2], time2[0], time2[1], time2[2], op)
if op == 1:
    t.sum()
elif op == 2:
    t.min() 
