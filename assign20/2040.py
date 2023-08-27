import logic

board_game = logic.start_game()

while True:
    inp = input("press the your command: ")

    if inp == "w":
        board_game, flag = logic.move_up(board_game)
        status = logic.get_current_state(board_game)
        print(status)
        if status == "Game Not Over":
            logic.add_new_2(board_game)
        else:
            break

    elif inp == "s":
        board_game, flag = logic.move_down(board_game)
        status = logic.get_current_state(board_game)
        print(status)
        if status == "Game Not Over":
            logic.add_new_2(board_game)

    elif inp == "a":
        board_game, flag = logic.move_left(board_game)
        status = logic.get_current_state(board_game)
        print(status)
        if status == "Game Not Over":
            logic.add_new_2(board_game)

    elif inp == "d":
        board_game, flag = logic.move_right(board_game)
        status = logic.get_current_state(board_game)
        print(status)
        if status == "Game Not Over":
            logic.add_new_2(board_game)

    else:
        print("Invalid Command!, Please try agane.")

    for game in board_game:
        print(game) 
