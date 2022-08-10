# -*- coding: UTF-8 -*-

from datetime import date

def calculateAge(birthDate):
    """
    age retona a idade atual do user aparti de uma subtracao do ano atual pro ano
    de nacimento today se refere a tada atual e birthDate a tada de nacimento subtraindo
    ano atual de ano de nacimedo assim tendo a idade,pra dar uma idade mais precisa
    verificamos se o mês e a data atuais são menores que o mês e a data de nascimento.
    Se sim, subtraia 1 da idade, caso contrário, 0.
    """
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

    return age

if __name__ == "__main__":
    nome = input ("Como se chama? ")
    ano = eval (input ("Nasceu em que ano? "))
    mes = eval (input ("Nasceu em que mês? "))
    dia = eval (input ("Nasceu em que dia? "))
    print(nome," is ",calculateAge(date(ano,mes,dia)), "years old")
