matrix = [input().split() for row in range(8)]
hit = False
queen = None


def check_row(queen, matrix, hit):
    for ind in range(queen[0], -1, -1):
        if matrix[queen[0]][ind] == "Q":
            break
        if matrix[queen[0]][ind] == "K":
            hit = True
    for ind in range(queen[0]+1, 8):
        if matrix[queen[0]][ind] == "Q":
            break
        if matrix[queen[0]][ind] == "K":
            hit = True
    return hit


def check_col(queen, matrix, hit):
    for ind in range(queen[1], -1, -1):
        if matrix[ind][queen[1]] == "Q":
            break
        elif matrix[ind][queen[1]] == "K":
            hit = True
    for ind in range(queen[1]+1, 8):
        if matrix[ind][queen[1]] == "Q":
            break
        elif matrix[ind][queen[1]] == "K":
            hit = True
    return hit

# def check_for_queen(n,m,matrix, queen):
#     if matrix[n][m] == "Q":
#         queen = [n, m]
#         return queen

for n in range(8):
    for m in range(8):
        if matrix[n][m] == "Q":
            queen = [n, m]
            hit = check_col(queen, matrix, hit)
            hit = check_row(queen, matrix, hit)
            if hit:
                print(queen)
            hit = False
