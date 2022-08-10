class Cliente:
    def __init__(self, nome, ida):
        self.nome=nome
        self.ida=ida
        self.enderecosos=[]

    def insereEndereco(self, cidade, estado):
        self.enderecosos.append(Endereco(cidade, estado))

    def listaEndereco(self):
        for endereco in self.enderecosos:
            print(endereco.cidade, endereco.estado)
    def __del__(self):
        print(f'{self.nome} FOI APAGADO')

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade=cidade
        self.estado=estado
    def __del__(self):
        print(f'{self.cidade}/{self.estado} FOI APAGADO')
