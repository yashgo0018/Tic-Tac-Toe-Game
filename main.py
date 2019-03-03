game_not_over = True

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

players = ({"name": "", "token": "X", "index": 0},
           {"name": "", "token": "O", "index": 1})

player_fault = False


def toggle_game_over(game_over):
    return not game_over


def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def handle_turn():
    position = input("Choose a position form 1-9: ")
    index = int(position) - 1
    # setting the user token on the position if blank
    if board[index] == "-":
        board[index] = current_player.get("token")
    else:
        global player_fault
        player_fault = True
        print("That Place is Already Occupied")
    display_board()


def flip_player():
    global current_player
    current_player = players[0] if current_player.get("index") == 1 else players[1]


def check_if_win():
    pass


def check_if_tie():
    pass


def check_if_game_over():
    check_if_win()
    check_if_tie()


def play_game():
    # Declaring the global vars
    global current_player, player_fault

    # Get Player Names
    players[0]["name"] = input("Player 1 Name: ")
    players[1]["name"] = input("Player 2 Name: ")

    # Setting the current player to the player 1
    current_player = players[0]

    # display initial board
    display_board()

    while game_not_over:
        handle_turn()
        # If game over terminate the game
        check_if_game_over()
        if not player_fault:
            flip_player()
        else:
            # Resetting the player fault for next time
            player_fault = False


play_game()
