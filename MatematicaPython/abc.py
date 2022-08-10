"""
Dev:@Kairo
Date:07/11/21
time:16h44
Alteracao:
    Date:20/11/21
    time:08h55
"""


def questao_a_ou_b(numero, numerador, end):
    """
    questoes a e b
    :numero: valor de inicio do laco
    :numeraodr: valor de incremento do laco
    :end: valor de inceramento do laco
    """

    if numerador == 1:
        print("\nA) Apresentar o total da soma obtida dos cem primeiros\
        \nnúmeros inteiros (1+2+3+4+...+98+99+100).\n")

    else:
        print("\nB) Elaborar um programa que apresente no final o somatório\
        \ndos valores pares existentes na faixa de 10 até 300.\n")

    new = 0
    quer = input("deseja ver todo o calculos\
    \naperta y pra sim e enter pra nao: ")
    while numero <= end:
        soma = numero+new
        if quer in ('y', 's'):
            print(numero, '+', new, '=', soma)
        numero = numero+numerador
        new = soma
    print("resutado toral da soma: ", soma)


def questao_c():
    """
    questão c
    """

    print("\nC) Apresentar todos os valores numéricos inteiros ímpares ituados\
    \nna faixa de 0 a 50.")
    print("Para verificar se o número é ímpar,efetuar dentro da malha a verifi\
cação lógica desta condição com a instrução se,")
    print("perguntando se o número é ímpar sendo, mostre-o; não sendo, passe p\
ara o próximo passo.\n")
    ini = 0
    impar = []
    while ini < 51:
        if ini == 0:
            print("valoz 0")

        if (ini % 2) != 0:
            impar += [ini]

        # else:
            # print("par:",ini)
        ini = ini+1
    rimpar = str(impar)[1:-1]
    print("numerais impares entre 0 e 50: ", rimpar)


print("qual questao deseja executar?")
QUESTAO = input("a b c ou a uniao deles ex: ab bc..: ").lower()
NUMA = 1
ENDA = 100
NURA = 1

NUMB = 10
ENDB = 300
NURB = 2

if QUESTAO in ('abc', 'acb', 'cba', 'cab', 'bac', 'bca'):
    questao_a_ou_b(NUMA, NURA, ENDA)
    questao_a_ou_b(NUMB, NURB, ENDB)
    questao_c()

elif QUESTAO == 'a':
    questao_a_ou_b(NUMA, NURA, ENDA)

elif QUESTAO == 'b':
    questao_a_ou_b(NUMB, NURB, ENDB)

elif QUESTAO == 'c':
    questao_c()

elif QUESTAO in ('ab', 'ba'):
    questao_a_ou_b(NUMA, NURA, ENDA)
    questao_a_ou_b(NUMB, NURB, ENDB)

elif QUESTAO in ('ac', 'ca'):
    questao_a_ou_b(NUMA, NURA, ENDA)
    questao_c()

elif QUESTAO in ('bc', 'cb'):
    questao_a_ou_b(NUMB, NURB, ENDB)
    questao_c()

else:
    print("eu falei a, b ou c")
