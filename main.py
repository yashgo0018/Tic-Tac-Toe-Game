game_over = False

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

players = ({"name": "", "token": "X", "index": 0},
           {"name": "", "token": "O", "index": 1})

player_fault = False

winner = {}


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


def check_rows():
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        token = board[0 if row1 else 3 if row2 else 6]
        return players[0 if token == "X" else 1]


def check_columns():
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    if col1 or col2 or col3:
        token = board[0 if col1 else 1 if col2 else 2]
        return players[0 if token == "X" else 1]


def check_diagonals():
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"
    if diagonal1 or diagonal2:
        token = board[0 if diagonal1 else 2]
        return players[0 if token == "X" else 1]


def check_if_win():
    global winner, game_over
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    winner = row_winner if row_winner else column_winner if column_winner else diagonal_winner if diagonal_winner else {}
    if winner.get("name"):
        game_over = True


def check_if_tie():
    global game_over
    if "-" not in board and not game_over:
        game_over = True


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

    while not game_over:
        handle_turn()

        # If game over terminate the game
        check_if_game_over()

        if not player_fault:
            flip_player()
        else:
            # Resetting the player fault for next time
            player_fault = False

    print(f"{winner.get('name')} won the game." if winner.get("name") else "The game was a draw.")


play_game()
