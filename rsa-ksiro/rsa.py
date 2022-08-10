# -*- coding: utf-8 -*-
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


def primo(pqprimo):
    '''
    essa def verifica se o valor corresponde a um numero primeiro
    pqprimo: valor a ser verificado
    conte: conta numero de divisores pqprimo tem
    percuso: conta de 1 ate pqprimo, para correr o while
    '''
    # pqprimo = int(input("inserir valor: "))
    conte = 0
    percuso = 1

    while percuso < (pqprimo + 1):
        if (pqprimo % percuso) == 0:
            conte += 1
        percuso += 1
    if conte == 2:
        print(" [primo]")
    else:
        print(" [não é primo]")
        pqprimo = int(input("coloca um valor valido: "))
        return pqprimo


print("="*12, "[RSA ]", "="*12)
p = int(input(" p: "))
pri = print(primo(p))
q = int(input(" q: "))
qpri = print(primo(q))
z = (p-1)*(q-1)
n = p*q
if p > q:
    primos = []
    for x in range(q, p):
        CONT = 0
        for y in range(1, x + 1):
            if x % y == 0:
                CONT += 1
        if CONT <= 2:
            primos.append(x)
            if mdc(z, x) == 1:
                e1 = int((z+1)/x)
                f = e1*x
                if f % z == 1:
                    print("="*24)
                    print(" e = (e*d) %z = ", f % z)
                    print(" ACHEI O e: ", e1)
                    print("\n Nesse caso d é: ", x)
                    print("="*24)
                    e = e1
                    d = x
    print(" primos entre q e p:\n", primos)
elif q > p:
    primos = []
    for x in range(p, q):
        CONT = 0
        for y in range(1, x + 1):
            if x % y == 0:
                CONT += 1
        if CONT <= 2:
            primos.append(x)
            if mdc(z, x) == 1:
                e1 = int((z+1)/x)
                f = e1*x
                if f % z == 1:
                    print("="*24)
                    print(" e = (e*d) %z = ", f % z)
                    print(" ACHEI O e: ", e1, "\n Nesse caso d é: ", x)
                    print("="*24)
                    e = e1
                    d = x
    print(" primos entre p e q:\n", primos)
else:
    print(" sao o mesmo numero ")
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
