#create a 9*9 soduko puzzle
from random import sample
import numpy as np

base = 3
side = base * base

# pattern for a baseline valid solution
def pattern(r, c): return (base * (r % base) + r // base + c) % side

# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s): return sample(s, len(s))

rBase = range(base)
rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
nums = shuffle(range(1, base * base + 1))

# produce board using randomized baseline pattern
def generate_board():
    return [[nums[pattern(r, c)] for c in cols] for r in rows]

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid(soduko, row, col, num):
    #check if the number is not in the current row
    if num in soduko[row]:
        return False
    #check if the number is not in the current column
    if num in soduko[:,col]:
        return False
    #check if the number is not in the current 3*3 grid
    start_row = 3* (row//3)
    start_col = 3* (col//3)
    if num in soduko[start_row:start_row +3, start_col:start_col+3]:
        return False
    return True


def create_soduko():
    soduko = np.zeros((9, 9))
    for i in range(9):
        for j in range(9):
            num_list = list(range(1, 10))
            while True:
                random.shuffle(num_list)
                for num in num_list:
                    if is_valid(soduko, i, j, num):
                        soduko[i, j] = num
                        break
                else:
                    continue
                break  
    return soduko

print (print_board(generate_board))
