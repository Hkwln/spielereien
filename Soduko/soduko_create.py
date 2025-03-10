import random
import torch

def is_valid(sudoku, row, col, num):
    # Check if the number is not in the current row
    if num in sudoku[row]:
        return False
    # Check if the number is not in the current column
    if num in sudoku[:, col]:
        return False
    # Check if the number is not in the current 3x3 grid
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    if num in sudoku[start_row:start_row + 3, start_col:start_col + 3]:
        return False
    return True

def fill_in(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row, col] == 0:
                num_list = list(range(1, 10))
                random.shuffle(num_list)
                for num in num_list:
                    if is_valid(sudoku, row, col, num):
                        sudoku[row, col] = num
                        if fill_in(sudoku):
                            return True
                        sudoku[row, col] = 0
                return False
    return True

def create_sudoku():
    sudoku = torch.zeros((9, 9), dtype=torch.int32, device='cuda')
    if not fill_in(sudoku):
        print("Failed to fill the Sudoku grid")
    return sudoku

# Example usage
sudoku = create_sudoku()
print(sudoku.cpu().numpy())
