class CarroDC:
    def __init__(self):
        self.produtos=[]
    def inserirProdutos(self, produto):
        self.produtos.append(produto)
    def listaProduto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def somaTotal(self):
        total=0
        for produto in self.produtos:
            total+=produto.valor
        return total

class Produto:
    def __init__(self, nome, valor):
        self.nome=nome
        self.valor=valor

