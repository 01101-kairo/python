#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @name: problema1
    @dave: Kairo
    @email: kosta.kairo@gmail.com
    @github: https://github.com/01101-kairo/
    @creation: 19/12/24 12h26
    @change: 19/12/24 12h
"""


def multiplo(cond):
    """
    @Description: Se listarmos todos os números naturais abaixo de 10 que
    são múltiplos de 3 ou 5, obtemos 3, 5, 6 e 9. A soma desses múltiplos
    é 23.
    Encontre a soma de todos os múltiplos de 3 ou 5 abaixo de 1000.
    https://projecteuler.net/problem=1
    """
    cont = 3
    soma = 0
    while cont < cond:
        if cont % 3 == 0 or cont % 5 == 0:
            soma = cont+soma
        cont = cont + 1
    return soma

if __name__=="__main":
    print(multiplo(1000))
