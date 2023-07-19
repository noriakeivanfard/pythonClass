names = input("enter files name: ")

names = names.split(" ")

for n in names:
    f = 0
    c = 0
    if "." in n:
        n = n.split(".")
        for i in ("0","1","2","3","4","5","6","7","8","9"):
            if i in n[1]:
                print(f"There is a number{names} in the file")
                f += 1
                break

        if len(n[1]) == len(n[1]) > 3:
            print(f"The problem is with the file letters{names}")
            f += 1
        
        elif n[1] == "err":
            print(f"The {n} suffix is equal to 'err'")
            f += 1

    else:
        print(f"in {n} '.' not find")
        f += 1
    
    for i in ("0","1","2","3","4","5","6","7","8","9"):
        c += n.count(i)
        if c > 3:
            print(f"There are already three numbers available {names}")
            f += 1
            break

    for i in ("0","1","2","3","4","5","6","7","8","9"): 
        if n[0] == i:
            print(f"name {n} starts a number")
            f += 1
    
    if f == 0:
        print(f"{n} acceptable")
    else:
        print(f"{n} is not acceptable")
