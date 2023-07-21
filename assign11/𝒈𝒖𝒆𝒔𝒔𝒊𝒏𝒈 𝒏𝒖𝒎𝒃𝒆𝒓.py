player1 = "player 1"
player2 = "player 2"
number = int(input('player1: enter youre number:'))
def check(number, number_i, player1, player2):
    if number < number_i:
        return "payintar"
    elif number > number_i:
        return "balatar"
    elif number == number_i:
        player_ = player1
        player1 = player2
        player2 = player_
        return  player1, player2


while True:
    number_i = int(input('player2:your number?'))
    if number_i == number:
      print('baba barikala')
      break
    elif number_i > number:
       print('payintar')
    else:
        print('balatar')
