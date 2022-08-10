# -*- coding: utf-8 -*
'''
dono: Kairo Milhomem Costa
programa: RSA criptografia com numeros primos
criado: 18/09/21 09h10
alterado: 24/09/21 13h59
'''

def mdc(avalor, bvalor):
    '''
    essa def tira o mdc
    '''
    if bvalor == 0:
        return avalor
    resto = avalor % bvalor
    return mdc(bvalor, resto)


def primo(pqnumero):
    '''
    essa def verifica se o valor corresponde a um pqnumero primeiro
    pqprimo: valor a ser verificado
    conte: conta numero de divisores pqprimo tem
    percuso: conta de 1 ate pqprimo, para correr o while
    numero primo opresor
    '''
    # numero = int(input("inserir valor primo: "))
    PERCUSO = 1
    CONT = 0
    VALID = True

    while PERCUSO < (pqnumero + 1):
        if (pqnumero % PERCUSO) == 0:
            CONT += 1
        PERCUSO += 1
    if CONT == 2 or pqnumero == 1:
        VALID = False
        print("primo")
    else:
        VALID = True
        print("no prime")
        CONT = 1
        while VALID:
            pqnumero = int(input("nuber prime: "))

            while PERCUSO < (pqnumero + 1):
                if (pqnumero % PERCUSO) == 0:
                    CONT += 1
                PERCUSO += 1
            if CONT == 2:
                VALID = False
                print("primo")
            else:
                VALID = True
                print("no prime")
                CONT = 1
            return pqnumero




def valores(maiovalor, menorvalor):
    """
    descobre os valores d e
    """
    if menorvalor > maiovalor:
        primos = []
        for percore in range(maiovalor, menorvalor):
            cont = 0
            for percusoy in range(1, percore + 1):
                if percore % percusoy == 0:
                    cont += 1
            if cont <= 2:
                primos.append(percore)
                if mdc(z, percore) == 1:
                    valortempe = int((z+1)/percore)
                    mutiplica = valortempe*percore
                    if mutiplica % z == 1:
                        print("="*24)
                        print(" e = (e*d) %z = ", mutiplica % z)
                        print(" ACHEI O e: ", valortempe)
                        print("\n Nesse caso d é: ", percore)
                        print("="*24)
                        valore = valortempe
                        valord = percore
                        return valore, valord
        print(" primos entre maiovalor e menorvalor:\n", primos)
    else:
        print(" [ERRO] ")


print("="*12, "[RSA ]", "="*12)
p = int(input(" p: "))
print(primo(p))
q = int(input(" q: "))
print(primo(q))
z = (p-1)*(q-1)
n = p*q

if p > q:
    print(valores(q, p))
    e = q
    d = p
elif q > p:
    print(valores(p, q))
    e = p
    d = q
else:
    print(" [ERRO] ")
print("="*24)
print(" z:", z, "\n e: ", e, "\n n:", n)
print("="*24)
x = int(input(" insert number: "))
cifra = (x**e)
y = cifra % n
frar = (y**d)
deci = frar % n
print("\n chave publica E e N:", e, "e", n)
print("\n chave privada D e N:", d, "e", n)
print("="*24)
# print("\n", x, "^e: ", cifra, "\n")
print(" cifra: ",  y)
# print("\n y ^e: ", frar, "\n")
print(" decifrar: ", deci)
print("="*24)
