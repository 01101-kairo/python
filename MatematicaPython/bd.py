"""
public, protected, private
_protected(naverdade é public é só uma aviso pra saber que ñ é pra mecher) 
__private
"""
class BancoDD:
    def __init__(self):
        self.__dados={}

    @property
    def dados(self):
        return self.__dados

    def inserirCliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes']={id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def listaClientes(self, id):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apagaCliente(self, id):
        del self.__dados['clientes'][id]

bd=BancoDD()
bd.inserirCliente(1, 'fernanda')
bd.inserirCliente(2,  'sofia')
bd.inserirCliente(5,'carlos')
bd.inserirCliente(7, 'emanuel')
bd.apagaCliente(2)
bd.listaClientes(id)
print(bd.__dados)