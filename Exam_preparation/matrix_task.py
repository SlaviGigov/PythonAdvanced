from collections import deque


def read_input():
    rows_count, columns_count = [int(x) for x in input().split()]
    lair = []
    for _ in range(rows_count):
        lair.append(list(input()))
    directions = input()
    return (lair, directions)


def get_bunnies(lair):
    for row_index in range(len(lair)):
        for column_index in range(len(lair[0])):
            if lair[row_index][column_index] == "B":
                bunnies.append((row_index, column_index))
    return bunnies


def get_player(lair):
    for row_index in range(len(lair)):
        for column_index in range(len(lair[0])):
            if lair[row_index][column_index] == "P":
                return (row_index, column_index)


def in_range(value, max_value):
    return 0 <= value <= max_value


def spread_bunnies(lair, bunnies):
    rows_count = len(lair)
    columns_count = len(lair[0])
    for _ in range(len(bunnies)):
        bunny = bunnies.popleft()
        next_bunnies = [
            get_next_move(bunny, dir)
            for dir in "UDLR"
        ]
        next_bunnies = [
            (row_index, column_index)
            for (row_index, column_index) in next_bunnies
            if in_range(row_index, rows_count) \
            and in_range(column_index, columns_count) \
            and lair[row_index][column_index] != "B"
        ]
        for next_bunny in next_bunnies:
            lair[next_bunny[0]][next_bunny[1]] = "B"
            bunnies.append(next_bunny)


def get_next_move(positions, dir):
    dir_deltas = {
        "U": (-1, 0),
        "D": (+1, 0),
        "L": (0, -1),
        "R": (0, +1),
    }
    (row_index, column_index) = player
    delta = dir_deltas[dir]
    return row_index + delta[0], column_index + delta[1]


def is_win(lair, plair):
    (row_index, column_index) = player
    return not in_range(row_index, len(lair)) or not in_range(column_index, len(lair[0]))


def is_loss(lair, player):
    (row_index, column_index) = player
    return lair[row_index][column_index] == "B"


def play_game(lair, bunnies, player, directions):
    bunnies = deque(bunnies)
    row_index, column_index = player
    for dir in directions:
        spread_bunnies(lair, bunnies)
        next_row_index, next_column_index = get_next_move(player, dir)
        if is_win(lair, (next_row_index, next_column_index)):
            lair[row_index][column_index] = "."
            print_result(lair, row_index, column_index, is_win=True)
            break
        elif is_loss(lair, (next_row_index, next_column_index)):
            print_result(lair, next_row_index, next_column_index, is_win=False)
            break
        lair[next_row_index][next_column_index] = "P"
        lair[row_index][column_index] = "."
        row_index, column_index = next_row_index, next_column_index


def print_result(lair, row_index, column_index, is_win):
    [print("".join(row)) for row in lair]
    print(row_index, column_index)
    print(is_win)


lair, directions = read_input()
bunnies = get_bunnies(lair)
player = get_player(lair)
play_game(lair, bunnies, player, directions)
