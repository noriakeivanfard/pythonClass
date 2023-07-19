import random

words = [["cat", "turtle", "dog", "elephant" , "kitten", "scorpian", "monkey", "lion","ant","rabbit"],
    ["orange","yellow","green","red","black","gray","white","pinck","blue","purple"],
    ["Samand","pride","Tiba","Dana","Benz","Lamborghini","Santafe","Saina","Persia","joke"],
    ["Mashhad","Tabriz","Tehran","Chabahar","Rasht","Lahijan","Sari","Shiraz","Kermanshah","Chabahar"],
    ["mango","Pineapple","Strawberry","watermelon","Apple","banana","grape","Peach","cherry","Orange"]]

W = int(input("1= Animals\n2= color\n3= cars\n4= citys\n5= fruits\n"))
word = random.choice(words[W-1])

user_word = [" _ " for i in range(len(word))]
hearts = [" ❤️ " for i in range(int(len(word) * 1.5)//1)]
show_word = []

while True:
    u_w = "".join(user_word)
    u_h = "".join(hearts)
    print(u_w)
    print(u_h)
    
    if str(u_w) == word:
       print("you win:)")
       break
    
    user_char = input("enter character : ")
    user_char = user_char.lower()

    for i in range(len(word)):
        if word[i] == user_char :
            user_word[i] = user_char 
            show_word.append(user_word)

    if user_char not in word:
        if user_char in show_word:
            print("You already guessed it")
            
        else:
         hearts = hearts[0:len(hearts)-1]
         show_word.append(user_char)
    if len(hearts) == 0:
        print("You lose:(")
        break
