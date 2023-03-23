import connect4_engine


def create_board(rows, cols):
    board = [[0 for _ in range(rows)] for _ in range(cols)]
    
    return board

def print_board(board):

    for r in range(0, len(board)):
        print(str(len(board) -r) + ": ", end='')
        for c in board[r]:
            print(c, end=" ")
        print()

    print("================")
    print("   A B C D E F G\n")

def board_data(board):
    data = []

    for c in range(len(board[0])-1, -1, -1):
        for r in range(0 , len(board)):
            data.append(board[r][c])

    data.reverse()

    return data

def play(player1, player2, board):
    print_board(board)

    while True:
        connect4_engine.take_turn(board, 1)
        print_board(board)
        connect4_engine.take_turn(board, 2)
        print_board(board)

if __name__ == "__main__":
    board = create_board(7, 6)
    play(1, 2, board)


    

    
