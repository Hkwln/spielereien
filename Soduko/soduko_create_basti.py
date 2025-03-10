import numpy as np
import time as t
import random
#check if value is permissible
def isValid(pos, value):
    #check row
    if value not in sudoku[pos//9]:
        #check column
        for y in range(9):
            if value == sudoku[y][pos%9]:
                return False
        if not inSquare(pos, value):
            return True
    else:
        return False

#check if value is in square
def inSquare(pos, value):
    x, y = (pos%9)//3, (pos//9)//3
    for iterY in range(3):
        for iterX in range(3):
            if sudoku[iterY+3*y][iterX+3*x] == value:
                return True
    return False


def fillInNext(pos):
    if pos == 81:
        print(f"Done! Here is your sudoku;\n{sudoku}")
        return True

    if sudoku[pos//9][pos%9]!=0:
        print("ERROR:")
        print(f"POS:{pos}\nGRID:\n{sudoku}")
        return None

    arr = np.arange(1, 10)
    random.shuffle(arr)

    for num in arr:
        if isValid(pos, num):
            sudoku[pos//9][pos%9]=num
            if fillInNext(pos+1):
                return True
            sudoku[pos // 9][pos % 9] = 0
    return False

start = t.perf_counter()
for _ in range(100):
    sudoku = np.zeros((9, 9), dtype=int)
    fillInNext(0)
end = t.perf_counter()
print(f"Average duration in seconds:{(end - start)/100:.6f}")