from classes import CarroDC, Produto

carrinho=CarroDC()

p1=Produto('comisa',500)
p2=Produto('chardineira',500)
p3=Produto('chote',500)
p4=Produto('jaqueta',500)

carrinho.inserirProdutos(p1)
carrinho.inserirProdutos(p2)
carrinho.inserirProdutos(p3)
carrinho.inserirProdutos(p4)

print (carrinho.listaProduto())
print (carrinho.somaTotal())