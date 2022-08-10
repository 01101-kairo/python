p = int(input("insert p:"))
q = int(input("insert q:"))
if p > q:
    primos = []
    for x in range(q, p):
        CONT = 0
        for y in range(1, x + 1):
            if x % y == 0:
                CONT += 1
        if CONT <= 2:
            primos.append(x)
    print(primos)
elif q > p:
    primos = []
    for x in range(p, q):
        CONT = 0
        for y in range(1, x + 1):
            if x % y == 0:
                CONT += 1
        if CONT <= 2:
            primos.append(x)
    print(primos)
else:
    print("sao o mesmo numero")
