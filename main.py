import os

os.system('clear    ')
board = []

def print_board():

    for i in range(9):
        for j in range(9):
            if j % 3 == 0 and j > 0:
                print("|",end='')
            print(" {0} ".format(board[i][j]),end='')
        print()
        if i % 3 == 2 and i > 0 and i != 8:
            print('---------+---------+---------')


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

def possible_numbers_in_box(row, column):
    possible_numbers = [a for a in range(1,10)]
    n_row = row
    n_column = column
    if n_row % 3 == 1:
        n_row -= 1
    elif n_row % 3 == 2:
        n_row -= 2
    if n_column % 3 == 1:
        n_column -= 1
    elif n_column % 3 == 2:
        n_column -= 2

    for i in range(3):
        for j in range(3):
            if board[n_row][n_column] != 0:
                possible_numbers.remove(board[n_row][n_column])
            n_column += 1
        n_column -= 3
        n_row += 1

    return possible_numbers

def find_possible_numbers_for_cell(row,column):
    if board[row][column] == 0:
        possible_column = possible_numbers_in_column(column)
        possible_row = possible_numbers_in_row(row)
        possible_box = possible_numbers_in_box(row, column)
        possible_numbers = list(set(possible_column) & set(possible_row) & set(possible_box))
        #print(possible_row,possible_column,possible_numbers)
        return possible_numbers

def solve():
    count = 0
    while count < 50:
        for i in range(9):
            for j in range(9):
                numbers = find_possible_numbers_for_cell(i,j)
                if type(numbers) == list and len(numbers) == 1:
                    board[i][j] = numbers[0]
        count += 1
        if not any(0 in sublist for sublist in board):
            break

    print("Algorithm called " + str(count) + " times.")

read_board()
print_board()
solve()
print("\n" + "-" * 10 + " Solved " + "-" * 10 + "\n")
print_board()
