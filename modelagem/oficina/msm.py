"""
essa é nossa calculadora python
"""
x = input('coloca uma variavel aqui x: / * - + .')
r = int(input('escreva aqui seu primeiro valor '))
y = int(input('escreva aqui seu segundo valor '))

if x == '+':
    M = r+y

elif x == '*':
    M = r*y

elif x == '-':
    M = r-y

elif x == '/':
    M = r/y

else:
    print("esses valores aqui q é pra vc escrever + * -")
print(M)
