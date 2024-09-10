# __dict__ e vars
# mantem um objeto do tipo mapping (dicionario) dentro do objeto
# é um atributo que mantem os valores que podem ser escritos dentro desse objeto
from datetime import date
DATA_ATUAL = date.today()

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return DATA_ATUAL.year - self.idade

p1 = Pessoa('Lucas', 19)
# p1.nome = 'Alterado'
# del p1.nome

print(p1.__dict__)
print(vars(p1))
# {'nome': 'Lucas', 'idade': 19}
# ambas retornam esse dicionario com chave e valor do que foi definido no 
# init desse objeto

# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'EITA'
# del p1.__dict__['nome']
# print(p1.__dict__)
# print(vars(p1))
# print(p1.outra)
# print(p1.nome)

# você pode fazer também dessa forma
dados = {'nome': 'Lucas', 'idade': 19}
p1 = Pessoa(**dados)
# p1 = Pessoa(nome= 'Lucas', idade = 19)

# desempacotando os kwargs