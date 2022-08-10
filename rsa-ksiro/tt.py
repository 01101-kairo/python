def valores(p, q):
    """
    descobre os valores d e
    """
    if q > p:
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
