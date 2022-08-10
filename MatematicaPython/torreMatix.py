"""
matix n por 3
i linha
j coluna
cada movimeto print matix pra exibir o movimeto.
[[#][x][x]
 [#][x][x]
 [#][x][x]]
"""

count = 0
def printtt(matx):
    for row in matx:
        print(row)


def moveT(altura, orig, dest, aux, mat):
    if altura >= 1:
        moveT(altura-1, orig, aux, dest, mat)
        moveD(orig, dest, mat)
        moveT(altura-1, aux, dest, orig, mat)


def moveD(s, f, m):
    global count
    count += 1
    print(f"{count}: {s} para {f}")
    for i in range(len(m)):
        if m[i][s] == '#':
            m[i][s] = 'x'
            break
    for i in range(len(m)):
        if i == len(m)-1 or m[i+1][f] == '#':
            m[i][f] = '#'
            break
    printtt(m)


n = int(input("quantos discos: "))
matix = [['#' if j == 0 else "x" for j in range(3)] for i in range(n)]
moveT(n, 0, 2, 1, matix)
