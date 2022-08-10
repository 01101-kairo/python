from cll import Cliente, Endereco
cliente1=Cliente('Alejandre',27)
cliente1.insereEndereco('Rio de janeiro','RJ')
print(cliente1.nome)
cliente1.listaEndereco()
print()
del cliente1

cliente2=Cliente('Marta',16)
cliente2.insereEndereco('Porto Frenco','MA')
print('\n'+cliente2.nome)
cliente2.listaEndereco()
print()
del cliente2

print('='*50)