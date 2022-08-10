"""
1 2 3 4 5 6 7
1 1 2 3 5 8 13
"""


def fib(n):
    """
    temporal -> O(n) -> Linear
    espacial -> O(1) -> Constante
    """
    if n <= 2:
        return 1
    inicial = 1
    secundario = 1
    contador = 0
    while contador < n-2:
        soma = inicial + secundario
        inicial = secundario
        secundario = soma
        contador += 1
    return soma


def rotate_matrix(matrix):
    """
    [[1, 4, 7]     [1, 4, 7]
     [2, 5, 6] ->  [2, 5, 8]
     [3, 8, 9]]    [3, 6, 9]

    [[1, 2, 3, 4]
    [5, 6, 7, 8]
    [9, 10, 11, 12] ->
    [13, 14, 15, 16]]

 i = 1, j = 0 -> i = 0, j = 1
 i = 1, j = 1 -> i = 1, j = 1
 i = 2, j = 2 -> i = 2, j = 2
 i = 2, j = 0 -> i = 0, j = 2

 (i, j) -> (new_i, new_j)


    temporal -> O(n^2) -> quadratico
    espaço -> O(n^2) -> quadratico
    """
    n = len(matrix)
    nova_matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            nova_matrix[j][i] = matrix[i][j]
    return nova_matrix


def rotate_matrix_const(matrix):
    """
    i linha
    j coluna
    [[1, 4, 7]     [0.0, 0.1, 0.2]
     [2, 5, 6] ->  [1.0, 1.1, 1.2]
     [3, 8, 9]]    [2.0, 2.1, 2.2]
    """
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i <= j:
                troca = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = troca
    return matrix


num = int(input("colocar valor:"))
amatrix = [[i for i in range(1 + num*(j-1), num*j+1)] for j in range(1, num+1)]
[print(row) for row in amatrix]
print("")
[print(row) for row in rotate_matrix_const(amatrix)]
