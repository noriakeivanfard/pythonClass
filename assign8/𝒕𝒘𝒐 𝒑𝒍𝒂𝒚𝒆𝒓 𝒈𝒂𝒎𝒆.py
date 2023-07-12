import random
number = int(input('player1: enter youre number:'))

while True:
    number_i = int(input('player2:your number?'))
    if number_i == number:
      print('baba barikala')
      break
    elif number_i > number:
       print('payintar')
    else:
        print('balatar')
