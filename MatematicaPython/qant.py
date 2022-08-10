
"""
Quantas senhas com 4 algarismos diferentes podemos escrever com os algarismos
1, 2, 3, 4, 5, 6, 7, 8,e 9?
"""
from fatorial import fatorial


def arranjo(N, P):
    """
    A = n!/(n-p)!
    """
    return fatorial(N)//fatorial(N-P)


def combinacao(N, P):
    """
    A = n!/p!(n-p)!
    """
    return fatorial(N)//(fatorial(P)*fatorial(N-P))


if __name__ == "__main__":
    n = int(input("N!: "))
    p = int(input("P!: "))
    print("arranjo: ", arranjo(n, p))
    print("combinacao: ", combinacao(n, p))
