# start from the KING
KING_SYMBOL = "K"
QUEEN_SYMBOL = "Q"


def read_board():
    board = [input().split() for _ in range(8)]
    return board


def find_king_position(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == KING_SYMBOL:
                return (row, col)


def in_range(value, max_value):
    return 0 <= value < max_value


def search_with_deltas(board, king, delta):
    rows_count = len(board)
    col_count = len(board[0])
    (row_ind, col_ind) = king
    (delta_row, delta_col) = delta
    while in_range(row_ind, rows_count) and in_range(col_ind, col_count):
        if board[row_ind][col_ind] == QUEEN_SYMBOL:
            return [row_ind, col_ind]

        row_ind += delta_row
        col_ind += delta_col

# Solution with separate directions:
# def get_winning_queens(board, king):
#     king_row_ind, king_col_ind = king
#     queens = []
#     # right
#     for col_index in range(king_col_ind + 1, 8):
#         if board[king_row_ind][col_index] == QUEEN_SYMBOL:
#             queens.append((king_row_ind, col_index))
#             break
#     # left
#     for col_index in range(king_col_ind - 1, -1, -1):
#         if board[king_row_ind][col_index] == QUEEN_SYMBOL:
#             queens.append((king_row_ind, col_index))
#             break
# Up = row + 1, col + 0
# down = -1, +0
# left-up diagonal +1, -1
# left-down diagonal -1,-1
# right-up diagonal -1+1
# right-down diagonal +1,+1
# return queens

def get_winning_queens(board, king):
    deltas = [
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
    ]
    queens = [search_with_deltas(board, king, delta) for delta in deltas]
    return [queen for queen in queens if queen]


def print_result(queens):
    if queens:
        for queen in queens:
            print(queen)
    else:
        print("The king is safe!")


board = read_board()
king = find_king_position(board)
queens = get_winning_queens(board, king)
print_result(queens)
