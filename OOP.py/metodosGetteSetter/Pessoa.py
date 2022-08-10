from random import randint

class Pessoa:
    ano_atual = 2020

    def __init__(self, nome, ida):
        self.nome = nome
        self.ida = ida

    def getAnoNacimento(self):
        print(self.ano_atual - self.ida)

    @classmethod
    def porAnoNacimento(cls, nome, anoNacimento):
        ida = cls.ano_atual - anoNacimento
        return cls(nome, ida)

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand

# p1=Pessoa.porAnoNacimento('kaima',1964)
p1 = Pessoa('kaima', 56)
print(p1)
print(p1.nome, p1.ida)
p1.getAnoNacimento()
print(Pessoa.gera_id())
print(p1.gera_id())
