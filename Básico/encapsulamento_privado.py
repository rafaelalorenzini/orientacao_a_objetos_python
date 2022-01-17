class Pessoa:

    def __init__(self,nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf
        # dois underlines torna o valor (atributo) cpf privado (sem acesso)

    def print_cpf(self):
        print(self.__cpf)   #consegue printar somente o que está sendo chamado pelo método

ronaldo = Pessoa('Ronaldo','32','3146482159')
print(ronaldo.nome)
print(ronaldo.idade)
print(ronaldo.cpf)
