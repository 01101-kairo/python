"""
Dev:Kairo
Date:22/10/20
time:13h44
"""
from datetime import date
from datetime import datetime
# from tkinter import messagebox
hota = datetime.now().strftime('%Hh%M')
DIAS = [
    'Seg',
    'Ter',
    'Qua',
    'Qui',
    'Sex',
    'Sáb',
    'Dom'
]
data_atual = date.today()
data = date(data_atual.year, data_atual.month, data_atual.day)
indice_da_semana = data.weekday()
dia_da_semana = DIAS[indice_da_semana]
numero_do_dia_da_semana = data.isoweekday()


# messagebox.showinfo(hota, dia_da_semana)
if dia_da_semana == "Seg":
    print("\n08h50:Biologia\n13h10:Geografia\n16h30:Ingles")
    if hota == '08h50':
        print("08h50 Biologia: ")
    if hota == '13h10':
        print("13h10 Geografia:\
              https://meet.google.com/ggc-inbx-wbi?authuser=1")
    if hota == '16h30':
        print("16h30 Ingles: ")

if dia_da_semana == "Ter":
    print("\n07h10:BD\n08h50:Portugues\n13h10:DEV Web")
    if hota == '07h10':
        print("07h10 BD: ")
    if hota == '08h50':
        print("08h50 Portugues: ")
    if hota == '13h10':
        print("13h10 DEV Web: ")

if dia_da_semana == "Qua":
    print("\n07h10:Redes\n13h10:Redes\n14h50:Quimica\n16h30:ED.Fisica")
    if hota == '07h10':
        print("07h10 Redes: ")
    if hota == '13h10':
        print("13h10 Seguranca: ")
    if hota == '14h50':
        print("14h50 Quimica: ")
    if hota == '16h30':
        print("16h30 ED.Fisica: ")

if dia_da_semana == "Qui":
    print("\n07h10:Redes\n10h30:Portugues\
          \n13h10:Matematica\n14h50:Oop\n16h30:ED")
    print("14h50:Oop\n16h30:Estrutura")
    if hota == '07h10':
        print("07h10 Redes: ")
    if hota == '10h30':
        print("10h30 Portugues: ")
    if hota == '13h10':
        print("13h10 Matematica: ")
    if hota == '14h50':
        print("14h50 Oop: ")
    if hota == '16h30':
        print("16h30 ED: ")

if dia_da_semana == "Sex":
    print("\n08h00:Filosofia\n09h40:Historia\
          \n13h10:Sociologia\n14h00:Artes\n17h20:Matematica")
    if hota == '08h00':
        print("08h00 Filosofia:\
              https://meet.google.com/scq-pjnp-wje?authuser=1")
    if hota == '09h40':
        print("09h40 Historia: ")
    if hota == '13h10':
        print("13h10 Sociologia: ")
    if hota == '14h00':
        print("14h00 Artes: ")
    if hota == '15h30':
        print("15h30 Fisica: ")
    if hota == '17h20':
        print("17h20 Matematica: ")
