from collections import deque
from math import ceil


def go_forward(row, cols, snake):
    for position in range(cols):
        matrix[row][position] = snake.popleft()
    return snake


def go_back(row, cols, snake):
    for position in range(cols - 1, -1, -1):
        matrix[row][position] = snake.popleft()
    return snake


def print_result(matrix):
    for r in range(rows):
        for c in range(cols):
            print(matrix[r][c], end="")
        print()


rows, cols = map(int, input().split())
matrix = [[0] * cols for _ in range(rows)]
snake = deque(input())
length = ceil(rows * cols / len(snake))
snake = snake * length

for r in range(rows):
    if r % 2 == 0:
        snake = go_forward(r, cols, snake)
    else:
        snake = go_back(r, cols, snake)

print_result(matrix)

# 100/100 nice job