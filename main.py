import os


board = []

def print_board():
    os.system('clear')
    for row in board:
        print(' '.join([str(x) for x in row ]))

def read_board():
    with open('sudoku.txt', 'r') as sudoku:
        for line in sudoku:
            board.append([int(a) for a in line.split()])

def possible_numbers_in_row(row):
    possible_numbers = [a for a in range(1,10)]
    for i in range(9):
        if board[row][i] != 0:
            possible_numbers.remove(board[row][i])
    return possible_numbers

def possible_numbers_in_column(column):
    possible_numbers = [a for a in range(1,10)]

    for i in range(9):
        if board[i][column] != 0:
            possible_numbers.remove(board[i][column])
    return possible_numbers

def find_possible_numbers_for_cell(row,column):
    if board[row][column] == 0:
        possible_column = possible_numbers_in_column(column)
        possible_row = possible_numbers_in_row(row)
        possible_numbers = list(set(possible_column) | set(possible_row))
        return possible_numbers



read_board()
print_board()
print(find_possible_numbers_for_cell(7,2))
