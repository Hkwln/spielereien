# Here i want to code how to calculate the inverse of a matrix using numpy

import numpy as np

# i know np.linalg.inv(matrix) calculates the inverse of a matrix directly
# but i want to code the inverse matrix like the formula A^-1 = 1/det(A) * adj(A)

# here you say if the matrix has modulo x
x = 5
# calculate the determinant of the matrix
def determinant(matrix):
    det = int(np.linalg.det(matrix)) % x
    if det == 0:
        print("The matrix has no determinant")
        return None
    print(det)
    return det 

# calculate the adjugate of the matrix
def cofactor(matrix):
    cofactor_matrix = np.zeros(matrix.shape, dtype=int)
    for row in range(matrix.shape[0]):
        for column in range(matrix.shape[1]):
            minor = np.delete(np.delete(matrix, row, axis=0), column, axis=1)
            cofactor_matrix[row, column] = ((-1) ** (row + column)) * int(np.linalg.det(minor)) % x
    return cofactor_matrix 

def adjugate(matrix):
    adj = np.transpose(cofactor(matrix)) % 5
    print(adj)
    return adj % x

# Calculate the modular inverse of a number modulo 5
def mod_inverse(a, mod):
    for x in range(1, mod):
        if (a * x) % mod == 1:
            return x
    raise ValueError(f"No modular inverse for {a} under modulo {mod}")

def inverse_matrix(matrix):
    det = determinant(matrix)
    
    if det is None:
        return None
    adj = adjugate(matrix)
    det_inv = mod_inverse(det, x) 
    inv = (det_inv* adj) %x
    print(inv)
    
    return inv % x
matrix = np.array([[1, 2, 1, 0], [1, 3, 0, 1], [0, 0, 4, 3], [2, 1, 2, 1]])

inverse_matrix(matrix)