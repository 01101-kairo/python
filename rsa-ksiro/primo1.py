def primo(numero):
    """
    numero primo opresor
    """
    PERCUSO = 1
    CONT = 0
    VALID = True
    # numero = int(input("inserir valor primo: "))

    while PERCUSO < (numero + 1):
        if (numero % PERCUSO) == 0:
            CONT += 1
        PERCUSO += 1
    if CONT == 2 or numero == 1:
        VALID = False
        print("sim primo", CONT)
    else:
        VALID = True
        print("nao prime")
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
            print("primo", CONT)
        elif CONT != 2:
            VALID = True
        else:
            print("como assim")
    print(numero)
    print("nao prime", CONT)


numero = int(input("inserir valor primo: "))
primo(numero)
