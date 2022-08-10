'''
dono: kairo Milhomem Costa
Programa: verificacao de numero primo
criado: 29/09/21 13h30
alterado: 29/09/21 17h11
'''
def primo(VALOR):
    CONT = 0
    PERCUSO = 1
    while PERCUSO < (VALOR + 1):
        if (VALOR % PERCUSO) == 0:
            CONT += 1
        PERCUSO += 1
    if CONT == 2:
        print(VALOR)
    else:
        print(2)


R = int(input(" p: "))
