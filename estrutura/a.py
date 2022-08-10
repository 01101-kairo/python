def fatorial(n: int) -> int:
    #caso base
    if n==1:
        return 1

    #caso recursivo
    return n*fatorial(n-1)

if __name__=="__main__":
    x=int(input("digite um valor:"))
    fat5= fatorial(x)
    print(fat5)

