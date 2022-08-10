from typing import List
from collections import namedtuple

Caixa = namedtuple('Caixa', 'temChave')


def encontraChave(caixas: List[Caixa], index: int = 0) -> Caixa:
    #caso base
    if len(caixas) <= index:
        return Caixa(False)

    caixa = caixas[index]

    #caso base
    if caixa.temChave:
        return caixa

    #caso recursivo
    index += 1
    return encontraChave(caixas, index)


if __name__ == "__main__":
    caixas: List[Caixa]=[
        Caixa(False), Caixa(False), Caixa(False), 
        Caixa(False), Caixa(True), Caixa(False), 
        Caixa(False), Caixa(False), Caixa(False), 
    ]
    
    print(encontraChave(caixas))

