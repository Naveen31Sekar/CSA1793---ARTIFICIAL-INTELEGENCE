def add_matrices(A, B):
    rows = len(A)
    cols = len(A[0])
    C = [[0 for row in range(cols)] for col in range(rows)]
    for i in range(rows):
        for j in range(cols):
            C[i][j] = A[i][j] + B[i][j]
    return C

A = [[1, 2, 3, 4]
     [4, 5, 6, 7]
     [7, 8, 9, 8]]
B = [[9, 8, 7,6]
     [6, 5, 4, 3]
     [3, 2, 1, 1]]

print(add_matrices(A, B))
