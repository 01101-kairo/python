#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @name: Untitled2
    @dave: Kairo
    @email: kosta.kairo@gmail.com
    @github: https://github.com/01101-kairo
    @creation: 21/12/12 16h47
    @change: 21/12/12 17h24
    @Description: Um programa que peça a quantidade em litros de
    um combustível, e o preço por litro, preços variáveis, e
    calcule o total em R$
"""


def litro(var):
    """
    descobrir quantos reais vai abastecer.
    """
    litros = float(input("Quantos litros vai abastecer: "))
    valor = litros*var
    print(f'{valor:.2f}', "R$")


def reais(var):
    """
    descobrir quantos litros vai abastercer.
    """
    valor = float(input("Quantos reais vai abastecer: "))
    litros = valor/var
    print(f'{litros:.2f}', "L")


GASOLINA_VAR = 3.50
QUAL = input("descobrir quantos [l]itros,\
\ndescobrir quantos [r]eais.\n").lower()
if QUAL == ('r'):
    litro(GASOLINA_VAR)
elif QUAL == ('l'):
    reais(GASOLINA_VAR)
else:
    print('não sei oque você quer')
