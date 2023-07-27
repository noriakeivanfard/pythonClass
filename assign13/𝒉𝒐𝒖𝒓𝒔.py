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
2_minus
which one?"""))

if op == 1:
    h = time1_dict["hour"] + time2_dict["hour"]
    m = time1_dict["minut"] + time2_dict["minut"]
    s = time1_dict["second"] + time2_dict["second"]
    
elif op == 2:
    h = time1_dict["hour"] - time2_dict["hour"]
    m = time1_dict["minut"] - time2_dict["minut"]
    s = time1_dict["second"] - time2_dict["second"]
    
def show_time(h,m,s):
    return f"{h}:{m}:{s}"
print(show_time(h,m,s))
