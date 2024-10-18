# escopo da classe
class Animal:
    def __init__(self,nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
    #     print(variavel)
# vai dar um erro pois a variavel está no escopo do init e não no da ação
        return f'{self.nome} está comendo {alimento}'
    
    def executando(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


leao = Animal(nome='leão')
print(leao.nome)
print(leao.comendo('Maçã'))
print(leao.executando('Maçã'))