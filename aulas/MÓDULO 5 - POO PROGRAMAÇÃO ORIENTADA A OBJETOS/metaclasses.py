# Metaclasses são um tipo das classes, esta acima de object
# EM PYTHON, TUDO É UM OBJETO(CLASSES TAMBEM SÃO)
#Então, qual é o tipo de uma classe? (type)
#Sue classe é uma instancia da sua classe
#sua classe é uma instancia de type (type é uma metaclass)
# from dataclasses import make_dataclass
# from networkx import octahedral_graph


# type('Name', (Bases,), __dict__)

# Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
# __new__ da metaclass é chamado e cria a nova classe 
# __call__ da metaclass é chamada com os argumentos e chama:
# chama os métodos
#      __new__ da class com os argumentos (cria a instância)
#     __init__ da class com os argumentos
# __call_da metaclass termina a execução

# Métodos importantes da metaclass 

# __new__(mcs, name, bases, dict) (cria a classe)

# __init__(cls, name, bases, dict) (cria a instância)

# __call__(cls, *args, **kwargs) (cria a instância e inicializa)

# "Metaclasses são magias profundas do que 99% dos usuários
# deveriam se preocupar. Se você quer saber se precisa deles
# não precisa(as pessoas que realmente precisam delas sabem 
# com certeza que precisam delas e não precisam de uma explicação sobre o porquê)"
#  - Tim Peters (CPython Core Developer)

#Object é herdado por herança
#o new que cria
#
class Foo:
    ...

# ou 
Foo = type('Foo',(object,),{})  # como é feito por debaixo dos panos


f = Foo() # é uma instancia da minha classe
print(isinstance(f, Foo)) #retorna true

print(type(Foo)) #retorna type

# type é uma metaclass
def meu_repr(self):
    return f'type{self.__name__}({self.__dict__})'


class Meta(type):
    def __init__(mcs,name,bases,dct):
        print("METACLASS NEW") #Primeira coisa a ser executada
        cls = super().__new__(cls)
        cls.attr = 1234
        cls.__repr__ = meu_repr()

        # print(cls.__dict__) você olha praticamente tudo que tem dentro da metaclass
        if 'falar' not in cls.__dict__ or not callable(cls.__dict__['falar']):
            raise NotImplementedError("implemente falar")

        return cls
    
    def __call__(cls, *args, **kwargs): # o call da metaclass são basicamente os parenteses
        instancia = super().__call__(*args, **kwargs)
        print(instancia.__dict__)
        
        if 'nome' not in instancia.__dict__:
            raise NotImplementedError("Crie o attr nome")
        return instancia
        

# class Pessoa(object, metaclass=type): por padrão é exatamente assim
class Pessoa(metaclass = Meta):
    def __new__(self, *args, **kwargs): # new cria a classe pessoa
        print("Meu New")
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self, nome):
        print("MEU INIT")
        self.nome = nome

    def falar (self):
        print("Falando")


p1 = Pessoa("Lucas")
print(p1.attr)
print(p1)

#resumindo o new cria e retorna a metaclass enquanto o call cria e retorna a instancia

