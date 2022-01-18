class MinhaClasse:

    estatico = 'Rafaela' #Variável de Classe

    def __init__(self, estado):
        self.estado = estado

    def print_estatico(self):
        print(self.estatico)
    @classmethod
    def mudar_estatico(cls):
        cls.estatico = 'programadora'  # cls = MinhaClasse -> fala da classe em si -> muda a variálvel de classe


obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)
print(obj1.estatico) # contexto de objeto -> Contexto Declarado
print(obj2.estatico) # contexto de objeto
print(MinhaClasse.estatico) # contexto de classe -> Contexto Geral

MinhaClasse.estatico = 'Programador'
obj1.estatico = 'rafaela'

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)

obj1.mudar_estatico()
obj1.print_estatico()