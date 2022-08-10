"""
recursão
Sobre o numero minimo de movimentos na torre:
n discos = 2^n-1 movimentos

objetivo:
    mover os discos do vetor A pro vetor C  com o auxilio do B

condisoes de movimento:
    nao pode mover para cima de um disco menor
    nao e possivel oculpa o lugar onde ja tem um disco

se disco for par, disco um vai pra vetor B
se disco for inpar, disco um vai pra vetor C
"""

count = 0
def moveT(altura, orig, dest, aux):
    if altura >= 1:
        moveT(altura-1, orig, aux, dest)
        moveD(orig, dest)
        moveT(altura-1, aux, dest, orig)
def moveD(s, f):
    global count
    count += 1
    print(f"{count}: {s} para {f}")


alt = int(input("quantos discos: "))
moveT(alt, 'a', 'c', 'b')
