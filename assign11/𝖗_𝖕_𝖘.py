import random

ask = input('play with friends or computer? (Enter f or c)')
n = int(input("1 or 3 or 5? "))
    
r_p_s = ["r", "p", "s"]
user1point = 0
computerpint = 0
user2point = 0

def check_player_computer(a , user1point, computerpint):
    if a == "user":
        user1point += 1
        return "user win:)", user1point, computerpint
    elif a == "computer":
        computer_c += 1
        return "computer win:)",user1point , computerpint
    else:
        return user1point , computerpint

def check_player_player(c, user1point , user2point ):
    if c == "player1 win ":
        user1point += 1
        return "user1 win:)", user1point,  user2point
    elif c == "player2":
        user2_c += 1
        return "user2 win", user1point,  user2point
    else:
        return  user1point,  user2point

if ask == 'c': 
    while (n != 0):
        computer = random.choice(r_p_s)
        user = input("rock(r) or paper(p) or scissors(s) \t") 
        if user == computer:
           print(f" computer selected {user}. It's a equal!")
           n = n - 1
        elif user == "r":
            if computer == "s":
                print("Rock smashes scissors! You win!")
                user1point = user1point + 1
                n = n - 1
            else:
                print("Paper covers rock! You lose.")
                computerpint = computerpint + 1
                n = n - 1
        elif user == "p":
            if computer == "r":
                print("Paper covers rock! You win!")
                user1point = user1point + 1
                n = n - 1
            else:
                print("Scissors cuts paper! You lose.")
                computerpint = computerpint + 1
                n = n - 1
        elif user == "s":
            if computer == "p":
                print("Scissors cuts paper! You win!")
                user1point = user1point + 1
                n = n - 1
            else:
                print("Rock smashes scissors! You lose.")
                computerpint = computerpint + 1
                n = n - 1
    if computerpint > user1point:
        print("The computer is winner :(")
    else:
        print("The user is winner :)")
elif ask == 'f':
    while (n != 0):
        computer = random.choice(r_p_s)
        user = input("rock(r) or paper(p) or scissors(s): Player 1\t") 
        user2 = input("rock(r) or paper(p) or scissors(s): Player 2\t") 

        if user == user2:
           print(f" player selected {user}. It's a equal!")
           n = n - 1
        elif user == "r":
            if user2 == "s":
                print("Rock smashes scissors! Player 1 win!")
                user1point = user1point + 1
                n = n - 1
            else:
                print("Paper covers rock! Player 2 win!")
                user2point = user2point + 1
                n = n - 1
        elif user == "p":
            if user2 == "r":
                print("Paper covers rock! Player 1 win!")
                user1point = user1point + 1
                n = n - 1
            else:
                print("Scissors cuts paper! Player 2 win!")
                user2point = user2point + 1
                n = n - 1
        elif user == "s":
            if user2 == "p":
                print("Scissors cuts paper!  Player 1 win!")
                user1point = user1point + 1
                n = n - 1
            else:
                print("Rock smashes scissors!  Player 2 win!")
                user2point = user2point + 1
                n = n - 1
    if user2point > user1point:
        print("The Player 2 is winner :)")
    else:
        print("The Player 1 is winner :)")
