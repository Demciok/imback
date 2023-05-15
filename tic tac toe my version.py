from random import randrange
board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
board1 = {1: (0, 0),
          2: (0, 1),
          3: (0, 2),
          4: (1, 0),
          5: (1, 1),
          6: (1, 2),
          7: (2, 0),
          8: (2, 1),
          9: (2, 2)}


def display_board(board):
    print(f"""
+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+""")


def enter_move(board):
    move = int(input("Podaj liczbe na ktorej chcesz postawic O (1-9)"))
    if board1[move] in make_list_of_free_fields(board):
        a, b = board1[move]
        board[a][b] = "O"


def make_list_of_free_fields(board):
    free_fields = []
    for column in board:
        for row in column:
            if row != "X" and row != "O":
                free_fields.append(board1[row])
    return free_fields


def victory_for(board, sign):
    win_numbers = [1, 2, 3], [4, 5, 6], [7, 8, 9], [
        1, 5, 9], [7, 5, 3], [1, 4, 7], [2, 5, 8], [3, 6, 9]
    for numbers in win_numbers:
        i = 0
        for a in numbers:
            d, e = board1[a]
            if board[d][e] == sign:
                i += 1
            if i == 3:
                print(f"Game wins the {sign} player")
                exit()
    print("tie or we keep playing")

# def victory_for(board,sign):
# for row in board:
#    if row[0]==row[1]==row[2]:
#    return True


def draw_move(board):
    draw = True
    while draw:
        k_move = randrange(1, 10)
        if board1[k_move] in make_list_of_free_fields(board):
            a, b = board1[k_move]
            board[a][b] = "X"
            draw = False


def game():
    while True:
        display_board(board)
        enter_move(board)
        victory_for(board, "O")
        display_board(board)
        draw_move(board)
        victory_for(board, "X")


game()

print(""" +-------+-------+-------+ | | | | | {} | {} | {} | | | | | +-------+-------+-------+ | | | | | {} | {} | {} | | | | | +-------+-------+-------+ | | | | | {} | {} | {} | | | | | +-------+-------+-------+ """.format(*
      [cell if cell != " " else i for i, cell in enumerate(board, start=1)]))
