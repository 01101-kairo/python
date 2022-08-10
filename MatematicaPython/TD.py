import datetime as td

print(td.time(21, 58, 6, 7),'Hora Minuto Segundo Microsegundo')
print(td.date(2022, 7, 16),'Ano Mes Dia')
print(td.datetime(2022, 7, 16,21, 58, 6, 7),'Ano Mes Dia Hora Minuto Segundo Microsegundo')

natal = td.date(2022,12,25)
reveillon = td.date(2023,1,1)

print(reveillon - natal)
print((reveillon - natal).days)
print((reveillon - natal).seconds)
print((reveillon - natal).microseconds)
