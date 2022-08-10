from classe import Escritor
from classe import Caneta
from classe import MaquinaDE

escritor=Escritor('maxado de assis')
caneta=Caneta('aguarela')
maquina=MaquinaDE()

escritor.ferramenta=caneta
escritor.ferramenta.escrever()

print(escritor.nome+' usa '+caneta.marca+' e está')
maquina.escrever()