from soduko_create import create_soduko, is_valid
import numpy as np

sudoku = create_soduko()
print("Generated sudoku")
print(sudoku)

# I want an algorithm that tries to solve the sudoku puzzle from soduko_create.py and checks it via the is_valid function from soduko_create.py
def solve_sudoku(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(sudoku, row, col, num):
                        sudoku[row][col] = num
                        if solve_sudoku(sudoku):
                            return True
                        sudoku[row][col] = 0
                return False
    return True

if solve_sudoku(sudoku):
    print("\nSolved Sudoku:")
    print(sudoku)
else:
    print("\nNo solution exists for the Sudoku puzzle.")