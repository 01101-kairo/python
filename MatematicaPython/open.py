def ler():
    arquivo = open('DC.txt','r')
    texto = arquivo.read()
    print(texto)
    arquivo.close()


def escrever():
    with open('kk.txt','w') as k:
        k.write('hahahahahaha\n')
    with open('kk.txt','r') as k:
        print(k.read(),end='')

ler()
