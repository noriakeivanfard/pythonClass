def vowels(st):
    st = input("enter string: ")
    for s in st:
        if   ord(s) ==  97 or ord(s) == 65: # a
            st = st.replace(s, "!")
        elif ord(s) == 101 or ord(s) == 69: # e
            st = st.replace(s, "!")
        elif ord(s) == 105 or ord(s) == 73: # i
            st = st.replace(s, "!")
        elif ord(s) == 111 or ord(s) == 79: # o
            st = st.replace(s, "!")
        elif ord(s) == 117 or ord(s) == 85: # u
            st = st.replace(s, "!")
    return st

print(vowels(1))
