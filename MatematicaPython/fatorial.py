"""
N!
5!= 5*4*3*2*1
"""


def fatorial(N):
    """
    fiz!!!
    """
    cot = N
    if N == 0:return 1
    while cot > 2:
        cot = cot - 1
        N = N * cot
        # print(N)
    return N

if __name__ == "__main__":
    print(fatorial(int(input("N!: "))))
