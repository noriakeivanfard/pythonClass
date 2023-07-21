import random

words = [["cat", "turtle", "dog", "elephant" , "kitten", "scorpian", "monkey", "lion","ant","rabbit"],
    ["orange","yellow","green","red","black","gray","white","pinck","blue","purple"],
    ["Samand","pride","Tiba","Dana","Benz","Lamborghini","Santafe","Saina","Persia","joke"],
    ["Mashhad","Tabriz","Tehran","Chabahar","Rasht","Lahijan","Sari","Shiraz","Kermanshah","Chabahar"],
    ["Avocado","mango","Pineapple","Strawberry","watermelon","Apple","banana","grape","Peach","cherry","Orange"]]

Category = int(input("1= Animals\n2= color\n3= cars\n4= citys\n5= fruits\nwhich one?"))
word = random.choice(words[Category-1])
word = word.lower()
print(word)

user_word = ["_" for i in range(len(word))]
h = ["❤️" for i in range(int(len(word) * 1.5))]
show_word = []

def show_h(h):
    u_h = "".join(h)
    return u_h

def show_w(w):
    u_w = "".join(w)
    return u_w

def check(word, w, show_word , h):
    if str(show_w(user_word)) == word:
        return "you win:)"
    
    if w not in word:
        if w in show_word:
            return "You already guessed it"
        else:            
            h = h[0:len(h)-1]
            show_word.append(w)
        
            if len(h) == 0:
                return "You lose:("
            
            return 1, h, show_word

w = ""
while True:
    s = check(word, w, show_word, h)
    if s != None:
        if s[0] == 1:
            h = s[1]
            show_word = s[2]
        else:
            print(s)
    
    if s == "you win:)" or s == "You lose:(":
        break

    print(show_w(user_word))
    print(show_h(h))

    w = input("enter character: ")
    w = w.lower()

    for i in range(len(word)):
        if word[i] == w:
            user_word[i] = w
            show_word.append(w)
