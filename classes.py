class PrimeiraClasse():
    def __init__(self, nome = "Desconhecido", idade = 0):
        self.___nome = nome
        self.__idade = idade
    
    def andar(self):
        print('Estou andando')

    @property
    def nome(self):
        return self.___nome

    @nome.setter
    def nome(self, nome):
        self.___nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

if __name__ == '__main__':
    pessoa1 = PrimeiraClasse()
    print(pessoa1.nome)
    print(pessoa1.idade)

    pessoa1.nome = "Julia"
    pessoa1.idade = 20

    pessoa1.andar()

    print(pessoa1.nome)
    print(pessoa1.idade)