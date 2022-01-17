class Pessoa: #subtantivo

    def __init__(self,nome: str, idade:int) -> None:
        self.nome = nome     #subtantivo
        self.idade = idade   #subtantivo

    def dirigir(self, veiculo: str) -> None: #verbo
        print(f'Dirigindo um(a) {veiculo}')

    def cantar(self) -> None : #verbo
        print('Lalalala')

    def apresentar_idade(self) -> int: #verbo
        return self.idade

