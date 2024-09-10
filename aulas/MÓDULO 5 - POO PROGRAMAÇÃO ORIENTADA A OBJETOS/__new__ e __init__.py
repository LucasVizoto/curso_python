# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e retornar o novo objeto. Por isso,
# new recebe cls. 

# __new__ ❗DEVE retornar o novo objeto❗
# __init__ é o método responsável por inicializar a instância. Por isso, init 
# receb self.
# __init__ ❗NÃO DEVE retornar nada(None)❗
# object é a super classe de uma classe

# SIMILAR A UM CONSTRUCTOR DE OUTRAS LINGUAGENS
# constructor é um método que cria um objeto
# new cria e o init inicializa o objeto

#A UTILIDADE DE DEFINIR UM NEW É PARA CASO VOCÊ QUEIRA FAZER ALGO ENTRE A CRIAÇÃO E A INICIALIZAÇÃO DO OBJETO
class A:
    def __new__(cls, *args, **kwargs):
        print('Coisas que estão acontecendo antes de criar a instancia')
        instancia = super().__new__(cls)
        print("Depois")
        instancia.x = 1805 #criando e tratando valores que deveriam estar no __init__
        return instancia

    def __init__(self, y):
        self.y = y
        print('Passou no init')
    
    def __repr__(self):
        return 'A()'

a = A(12)
print(a.x)
print(a.y)