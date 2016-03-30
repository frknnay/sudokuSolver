import os


board = []

for i in range(9):
    board.append(['?'] * 9) # Creates game board

def print_board(board):
    os.system('clear')
    for row in board:
        print(' '.join(row))

def fill_the_board():
    message = "Enter a number (X). Put '?' if you don't know the number: "
    for i in range(len(board)):
        for x in range(len(board[i])):
            board[i][x] = 'X'
            print_board(board)
            board[i][x] = input(message)


print_board(board)
fill_the_board()
