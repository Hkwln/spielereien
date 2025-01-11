#create a 9*9 soduko puzzle
import random
import numpy as cp
import time as t

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
def fill_in(soduko):
    for row in range(9):
        for col in range(9):
            if soduko[row, col] == 0:
                num_list = list(range(1, 10))
                random.shuffle(num_list)
                for num in num_list:
                    if is_valid(soduko, row, col, num):
                        soduko[row, col] = num
                        if fill_in(soduko):
                            return True
                        soduko[row, col] = 0
                return False
    return True

#lösche in random row oder column die zahlen und schreibe eine 0 rein
def delete_numbers(soduko, num_delete):
    num_list = list(range(0,9))
    for i in range(num_delete+1):
        random_row = random.choice(num_list)
        random_col = random.choice(num_list)
        soduko[random_row, random_col] = 0
    return soduko

def create_soduko():
    soduko = cp.zeros((9, 9), dtype=cp.int32)  
    #fill in the first 3*3 grid
    if not fill_in(soduko):
        print("Failed to fill the Sudoku grid")
    #solution_soduko = soduko.copy()
    #delete_numbers(soduko, 20)
    return soduko#, solution_soduko


start = t.perf_counter()
for _ in range(100):
    create_soduko()
end = t.perf_counter()
print(f"Average duration in seconds:{(end - start)/100:.6f}")