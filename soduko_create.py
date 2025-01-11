#create a 9*9 soduko puzzle
import random
import cupy as cp


def is_valid(soduko, row, col, num):
    #check if the number is not in the current row
    if num in soduko[row]:
        return False
    #check if the number is not in the current column
    if num in [soduko[i][col] for i in range(9)]:
        return False
    #check if the number is not in the current 3*3 grid
    start_row = 3* (row//3)
    start_col = 3* (col//3)
    for i in range(3):
        for j in range(3):
            if num == soduko[start_row + i][start_col + j]:
                return False
    return True
def fill_in_next(soduko):
    for row in range(9):
        for col in range(9):
            if soduko[row, col] == 0:
                num_list = list(range(1, 10))
                random.shuffle(num_list)
                for num in num_list:
                    if is_valid(soduko, row, col, num):
                        soduko[row, col] = num
                        if fill_in_next(soduko):
                            return True
                        soduko[row, col] = 0
                return False
    return True
def create_soduko():
    soduko = cp.zeros((9, 9), dtype=cp.int32)    
    #fill in the first 3*3 grid
    if not fill_in_next(soduko):
        print("Failed to fill the Sudoku grid")
    return soduko

soduko = create_soduko()
print(cp.asnumpy(soduko))

#Checks if the operation is on Gpu
print("Is the array on GPU?", cp.get_array_module(soduko) is cp)
print("Current device:", cp.cuda.Device().id)
