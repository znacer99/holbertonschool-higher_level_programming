#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    cols = len(matrix[0])
    matrix_squared = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            matrix_squared[i][j] = matrix[i][j] ** 2
    for row in matrix_squared:
        print(row)
