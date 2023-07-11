password_l = 1389
list_password = []
c = 1
bool = True
while bool:
    password = int(input('enter password:'))
    if password_l == password:
        print('log in')
        bool = False
    elif (password_l) == (list_password[::-1]):
        print('calling to police')
        bool = False
    elif c == 3:
        print("lock")
        bool = False
    else:
        print('please try again')
        c = c + 1
        
