import random


def print_board(board):
    for i in range(0, len(board), 3):
        print(f"{board[i]}{board[i + 1]}{board[i + 2]}")


def open_spots(board):
    spots = []
    for i in range(len(board)):
        if board[i] == "-":
            spots.append(i)

    return spots


def random_move(board, symbol):
    spots = open_spots(board)
    open_spot = random.choice(spots)
    board[open_spot] = symbol
    # print_board(board)


def check_three(board, idx1, idx2, idx3):
    symbol = "-"
    if board[idx1] == board[idx2] == board[idx3]:
        symbol = board[idx1]

    return symbol


def winner(board):
    combos = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    symbol = "-"
    for combo in combos:
        symbol = check_three(board, combo[0], combo[1], combo[2])
        if symbol != "-":
            break

    if len(open_spots(board)) == 0 and symbol == "-":
        symbol = "D"

    return symbol


def tic_tac_toe():
    board = ["-"] * 9
    player = "X"
    game_over = False
    win_symbol = "-"

    while not game_over:
        random_move(board, player)
        win_symbol = winner(board)
        if win_symbol != "-":
            game_over = True

        player = "O" if player == "X" else "X"

    return win_symbol


if __name__ == "__main__":
    x_wins = 0
    o_wins = 0
    draws = 0

    for i in range(1000):
        win_symbol = tic_tac_toe()
        if win_symbol == "X":
            x_wins += 1
        elif win_symbol == "O":
            o_wins += 1
        else:
            draws += 1

    print("X wins: ", x_wins)
    print("O wins: ", o_wins)
    print("Draws: ", draws)

    # winner(["X", "X", "O", "O", "X", "X", "O", "X", "O"])  # X
    # winner(["X", "-", "O", "X", "O", "-", "O", "-", "X"])  # O
    # winner(["O", "X", "O", "X", "X", "O", "X", "O", "X"])  # D
    # winner(["X", "X", "O", "-", "X", "-", "X", "O", "O"])  # -
    # winner(["-", "-", "-", "X", "X", "X", "O", "O", "-"])  # X
