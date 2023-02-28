import os
from random import randrange

BOARD_SIZE = 4

def clear_screen():
    n = os.name
    if n == 'nt': # windows
        os.system('cls')
    elif n == 'posix': # linux
        os.system('clear')
    else:
        print('system not supported')
        exit()

def new_board():
    board = []
    for i in range(BOARD_SIZE):
        row = [j+1 for j in range(BOARD_SIZE*i, BOARD_SIZE*(i+1))]

        if i == BOARD_SIZE - 1:
            board.append(row[:-1] + [0])
        else:
            board.append(row)
    return board

def shuffle_board(board, iter=1000):
    for _ in range(iter):
        n = randrange(1, BOARD_SIZE*BOARD_SIZE-1)
        board = move_n(board, n)
    
    return board

def draw_board(board):
    for i in range(BOARD_SIZE):
        print('|' + '|'.join('%2d'%j for j in board[i]) + '|' + '\n')

def check_board(board):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if i == j == BOARD_SIZE-1:
                return True

            if board[i][j] != i*BOARD_SIZE + j + 1:
                return False

def find_n(board, n):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == n:
                x, y = i, j
    
    return x, y

def move_n(board, n):
    x, y = find_n(board, n)

    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if not (0 <= x+dx < BOARD_SIZE and 0 <= y+dy < BOARD_SIZE):
            continue

        if board[x+dx][y+dy] == 0:
            board[x][y], board[x+dx][y+dy] = board[x+dx][y+dy], board[x][y]
            
            return board
    return board
    
def play():
    board = new_board()
    board = shuffle_board(board)

    while not check_board(board):
        clear_screen()
        draw_board(board)

        n = input(">>> ")
        try:
            n = int(n)
        except:
            continue

        board = move_n(board, n)
    
    clear_screen()
    draw_board(board)
    print("congratulations.")

if __name__ == '__main__':
    play()
