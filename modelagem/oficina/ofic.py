# -*- coding: utf-8 -*-
"""
programador: $kairo
linguagem: python3
utimaAtualização: 17/maio/2020
programa: louja de peçãs de uma oficina
falta: BD
"""
from operario import Operario
def login(nome,senha):#primeira função obijetivo intentificar usuario isso aqui é um BD inprovisado
    no1, no2, no3, no4 = "kairo","eduardo","joão","wladimir"#usuarios registrados
    n1, n2, n3, n4 = "gnu","abacaxi","ougod","imgay"        #senhas dos usuarios

    if nome == no1 :#IndentificandoUsuario
        if senha == n1:#IndentificandoSenhaDoUsuario
            return "\nO senhor tem permição total\n"        
        else: #NãoFoiIndentificandoSenhaDoUsuario
            return ERRO

    elif nome == no2 :#IndentificandoUsuario
        if senha == n2:#IndentificandoSenhaDoUsuario
            return "\nO senhor tem permição total\n"        
        else: #NãoFoiIndentificandoSenhaDoUsuario
            return  ERRO
    elif nome == no3:#IndentificandoUsuario
        if senha == n3:#IndentificandoSenhaDoUsuario
            return "\nO senhor tem permição intermediaria\n"
        else: #NãoFoiIndentificandoSenhaDoUsuario
            return  ERRO 
    elif nome == no4:#IndentificandoUsuario
        if senha == n4:#IndentificandoSenhaDoUsuario
            return "\nO senhor tem permição restrita\n"
        else: #NãoFoiIndentificandoSenhaDoUsuario
            return  ERRO
    else: #NãoFoiIndentificandoUsuario
        return  ERRO

print('-'*51)
desejo=input('[O que deseja \'logar\' ou \'criar\' uma conta]')
ERRO=('='*22+"[ERRO]"+'='*22+"\nSua informação esta incoerente senhor.\n")
print("\n")
if desejo=='logar':
    print('-'*22+'[Login]'+'-'*22+'\n')
    op1=name = input('[Seu nome: ] ')
    op1=passwords = input('[Sua senha:] ')
    print(login(name, passwords))#chamada da função
    print('='*51)
