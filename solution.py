import numpy as np

# check for the next empty cell on the board
def find_empty_cell(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                # return the empty cell by (row, col)
                return i, j
    return None

# row no repeat, col no repeat, 3X3 cell no repeat
def is_valid(sudoku, num, pos):
    '''
    num: the number inserted into
    pos: the position where needed to be inserted. (row, col)
    '''
    # check row
    for i in range(len(sudoku[0])):
        # the rest of the position in row contains the same num as the one just inserted into,
        if sudoku[pos[0]][i] == num and i != pos[1]:
            return False

    # check col
    for j in range(len(sudoku)):
        # the rest of the position in col contains the same num as the one just inserted into,
        if sudoku[j][pos[1]] == num and j != pos[0]:
            return False

    # check 3X3 cell
    # in which 3X3 cell
    cell_x = pos[1] // 3
    cell_y = pos[0] // 3

    # loop for the 3X3 cell, check for all the numbers
    for i in range(cell_y * 3, cell_y * 3 + 3):
        for j in range(cell_x * 3, cell_x * 3 + 3):
            # check for the rest of the numbers in this 3X3 cell
            if sudoku[i][j] == num and (i,j) != num:
                # contains the repeated num
                return False
    return True

# backtrack searching
def sudoku_solver(sudoku):
    # initial_sudoku = sudoku
    test_sudoku = np.copy(sudoku)
    # not fixed now
    ### backtrack algorithm
    found = find_empty_cell(test_sudoku)
    # basic case
    if not found:
        # no empty cells means we find the solution
        print(test_sudoku)
        return True
    else:
        # found an empty cell, so that can try nums (1~9)
        row, col = find_empty_cell(test_sudoku)

    for num in range(1, 10):
        if is_valid(test_sudoku, num, (row, col)):
            # insert the valid num into the board in the empty position
            test_sudoku[row][col] = num
            # check the new board after inserting one new number
            if sudoku_solver(test_sudoku):
                return True

            # backtrack, set it back to 0
            test_sudoku[row][col] = 0

    # backtrack to the previous position
    return False


# sudoku with no solution, set all the cells as -1
def no_solution(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            sudoku[i][j] = -1
    return sudoku
