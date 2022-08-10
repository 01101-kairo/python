"""
Dev: Kairo
Dat: 23/11/21
Clock:20h36
Desafio: o maximo divisor comum de dois inteiros e o maior numero que divide
ambos sem deixar resto. Escreva um programa q, dado dois inteiros, calcule o
seu maximo divisor comum.
"""
def mdc(a, b):
    """
    Esse e' o MDC
    """
    if a < b:
        return mdc(b, a)
    if b == 0:
        return a
    r = a % b
    return mdc(b, r)


intero1 = (int(input("manda a braba: ")))
intero2 = (int(input("manda a braba: ")))
mdc = mdc(intero1, intero2)
if intero1 > intero2:
    MAIOR = intero2
elif intero1 <= intero2:
    MAIOR = intero1
OR = 1
while OR <= MAIOR:
    if intero1 % OR == 0:
        if intero2 % OR == 0:
            EX = OR
    OR = OR + 1
print("MDC: ", mdc, "\nMaior divisor comum: ", EX)
