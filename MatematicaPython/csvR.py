import csv

with open('Bra.csv', 'r') as bra:
    leitor = csv.reader(bra)
    for linha in leitor:
        print(linha)