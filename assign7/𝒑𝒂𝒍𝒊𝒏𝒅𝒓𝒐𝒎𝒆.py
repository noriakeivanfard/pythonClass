str =  input("enter your string: ")
s = reversed(str)
S = "".join(s)

if S == str:
 print("is palindrom")
else:
 print("is not palindrom")
