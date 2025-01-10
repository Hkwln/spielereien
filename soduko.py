import numpy as np
from random import sample

base = 3
side = base * base

# pattern for a baseline valid solution
def pattern(r, c): 
    return (base * (r % base) + r // base + c) % side

# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s): 
    return sample(s, len(s))

rBase = range(base)
rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
nums = shuffle(range(1, base * base + 1))

# produce board using randomized baseline pattern
def generate_board():
    return [[nums[pattern(r, c)] for c in cols] for r in rows]

def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))

if __name__ == "__main__":
    board = generate_board()
    
    print("Sudoku Solution:")
    print_board(board)