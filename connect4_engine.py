def x_in_a_row(player_token, win_length, token_list):
    count = 0

    for i in range(0, len(token_list)):
        if token_list[i] == player_token:
            count += 1
            if count == win_length:
                return True
        else:
            count = 0
    
    return False


def get_ascending_diag(board, row, col):
    ascending = []

    start_row = row + col
    start_col = 0
    start_col = 0

    if start_row > len(board)-1:
        diff = start_row - (len(board)-1) 
        start_row -= diff
        start_col += diff

    next_row = start_row
    next_col = start_col

    while(next_row > 0 and next_col < len(board[0])):
        ascending.append(board[next_row][next_col])
        next_row -= 1
        next_col += 1

    return ascending


def get_descending_diag(board, row, col):
    descending = []
    start_row = row - col
    start_col = 0

    if start_row < 1:
        diff = 1 - start_row
        start_row += diff
        start_col += diff

    next_row = start_row
    next_col = start_col

    while(next_row < len(board) and next_col < len(board[0])):
        descending.append(board[next_row][next_col])
        next_row += 1
        next_col += 1

    return descending

def get_row(board, row_number):
    row = []
    for i in range(0, len(board[0])):
        row.append(board[row_number][i])

    return row

def get_col(board, col_number):
    col = []
    for i in range(0, len(board)):
        col.append(board[i][col_number])

    return col

def take_turn(board, player):

    while True:
        player_input = input(f"Player {player}'s turn: ")
        print()
        player_input = player_input.upper()

        if player_input == "Q":
            end_game(player, False)

        if get_labels().count(player_input) > 0:
            drop_token(board, player, column_label_to_index(player_input))
            break
        else:
            print("Invalid Column.")
            continue


def drop_token(board, player, column_index):
    if board[0][column_index] != 0:
        print("Column is full.")
        take_turn(board, player)
    else:
        i = len(board)-1
        while i > -1:
            if board[i][column_index] == 0:
                board[i][column_index] = player
                potential_wins = [
                    get_row(board, i),
                    get_col(board, column_index),
                    get_ascending_diag(board, i, column_index),
                    get_descending_diag(board, i, column_index)
                ]
                
                for j in potential_wins:
                    if x_in_a_row(player, 4, j):
                        end_game(player, True)
                break
            
            i -= 1

def column_label_to_index(column_label):
    labels_to_index = {
        "A": 0, 
        "B": 1,  
        "C": 2, 
        "D": 3,
        "E": 4, 
        "F": 5,
        "G": 6
    }

    return labels_to_index.get(column_label)

def get_labels():
    return ["A", "B", "C", "D", "E", "F", "G"]

def end_game(player, isWinner):
    if isWinner:
        print(f"Player {player} wins!")
    else:
        print(f"Player {player} ended the game...")
    
    exit(0)