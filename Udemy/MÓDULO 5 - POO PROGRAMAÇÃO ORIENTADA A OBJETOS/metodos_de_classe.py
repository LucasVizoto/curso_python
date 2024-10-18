#Métodos de Classe + factories
# são métodos onde 'self' será 'cls'(não é o que limpa o terminal, esse é o nome da classe), ou seja, ao invés
# de receber a instância no primeiro parâmetro, 
# receberemos a própria classe
from datetime import date
DATA_ATUAL = date.today()

class Pessoa:
    ano = DATA_ATUAL.year #atributo da classe
# um atributo solto está fora do escopo de um método
                  #usa o cookie, o produto do molde
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('fasdfasdf')

    @classmethod      #usa o molde, a classe em si
    def criar_com_50_anos(cls, nome):
        return cls(nome,50)

    @classmethod      #usa o molde, a classe em si
    def criar_sem_nome(cls, idade):
        return cls('Anônimo',idade)
# você não tem acesso a instancia dentro desse método, pq vc chama a classe enão uma instância

p1 = Pessoa('Lucas', 19)
p2 = Pessoa.criar_com_50_anos('Elienai') 
p3 = Pessoa.criar_sem_nome(23)
# factorie class é basicamente você criar um método que gere instancias prontas para você
# como ele recebe a classe ele pode usar ela para se chamar novamente
# basicamente o que tinha visto com decorator mas com as funções

print(p1.ano)
print(p2.nome, p2.ano)
p1.metodo_de_classe()


Pessoa.metodo_de_classe()
# como fazer isso sem passar parametros?? usando um decorator
# o @classmethod significa que você pode chamar a classe sem passar um self
# MAS é necessário insirir alguma coisa ali, então vc passa a própria classe como 'cls' 

#--------------------------------------------------------------------------------------------------------------------------------

# @staticmethod (métodos estáticos) (praticamente inúteis em Python)
# métodos estáticos são métodos que estão dentro da classe
# mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua classe

class Classe:
    @staticmethod
    def funcao_que_esta_dentro_da_classe(*args, **kwargs):
        print('OI', (args, kwargs))

# é literalmente a msm coisa

def funcao(*args, **kwargs):
    print('OI', (args, kwargs))    

c1 = Classe()
c1.funcao_que_esta_dentro_da_classe(1,2,3)

# a inutilidade disso é que é literalmente a criação de uma função, mas dentro da classe
# penso eu, no meu raciocínio inferior, que seja pra facilitar no from import 
