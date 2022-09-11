# -*- coding: utf-8 -*-
'''
dono: Kairo Milhomem Costa
programa: RSA criptografia com numeros primos
criado: 18/09/21 09h10
alterado: 01/10/21 14h28
'''


print("="*12, "[RSA]", "="*12)
p = int(input(" p: "))
PERCUSO = 1
CONT = 0
VALID = True
numero = p

while PERCUSO < (numero + 1):
    if (numero % PERCUSO) == 0:
        CONT += 1
    PERCUSO += 1
if CONT == 2 or numero == 1:
    VALID = False
    print("primo", CONT)
    p = numero
else:
    VALID = True
    print("no prime")
while VALID:
    numero = int(input("nuber prime: "))
    PERCUSO = 1
    CONT = 0

    while PERCUSO < (numero + 1):
        # print("no prime")
        if (numero % PERCUSO) == 0:
            CONT += 1
        PERCUSO += 1

    if CONT == 2 or numero == 1:
        VALID = False
        print("primo", numero, CONT)
        p = numero
    elif CONT != 2:
        VALID = True
    else:
        print("como assim")
print(numero)
print("no prime", CONT)
print("ok", p)
q = int(input(" q: "))
PERCUSO = 1
CONT = 0
VALID = True
numero = q

while PERCUSO < (numero + 1):
    if (numero % PERCUSO) == 0:
        CONT += 1
    PERCUSO += 1
if CONT == 2 or numero == 1:
    VALID = False
    print("primo", CONT)
    q = numero
else:
    VALID = True
    print("no prime")
while VALID:
    numero = int(input("nuber prime: "))
    PERCUSO = 1
    CONT = 0

    while PERCUSO < (numero + 1):
        # print("no prime")
        if (numero % PERCUSO) == 0:
            CONT += 1
        PERCUSO += 1

    if CONT == 2 or numero == 1:
        VALID = False
        print("primo", numero, CONT)
        p = numero
    elif CONT != 2:
        VALID = True
    else:
        print("como assim")
print(numero)
print("no prime", CONT)
print("ok", q)
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
                    print(" ACHEI O e: ", e1)
                    print("\n Nesse caso d é: ", x)
                    print("="*24)
                    e = e1
                    d = x
    print(" primos entre p e q:\n", primos)
else:
    print(" [ERRO]")
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

