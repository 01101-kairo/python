def invert(cdu):
    """
    vou somar dividir tirar resto pra inverter um inteiro de 3 digitos
    N = c*100 + d*10 + u*1.

    123 -> 321

    C|D|U
    1|2|3
    """
    c = cdu//100
    d = (cdu//10) % 10
    u = cdu % 10
    N = u*100 + d*10 + c*1
    print(N)


if __name__ == "__main__":
    invert(int(input("inteiro entre 100 e 999: ")))
