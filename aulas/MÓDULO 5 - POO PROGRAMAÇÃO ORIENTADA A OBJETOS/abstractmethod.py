#abstractmethod para qualquer metodo já criado
# é possivel criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso use 
# @abtractmethod como decorador mais interno.
# Foo - Bar são palavras usadas como placeholders
# para palavras que podem mudar na programação

from abc import abstractmethod, ABC 

class AbstracFoo(ABC):
    def __init__(self, name):
        self._name = None #vazio pq ainda não recebeu
        self.name = name

    @property #getter e o que é retornado
    @abstractmethod #o abstractmethod tem que vir o mais interno possivel
    def name(self): ... 
        # return self._name #retorna esse valor já altrerado pelo setter


class Foo(AbstracFoo):
    def __init__(self, name):
        super().__init__(name) 
        print('Sou inútil')# esse Init ele é inútil pois ele só passa o init para o init da classe super 
# sempre que definir um init em classes com herança, tomar cuidado com a sobreposição de inits
        
    @property
    def name(self):
        return self._name
    
    @name.setter 
    def name(self, value):
        self._name = value # alteração do vaslor para o retorno na property

foo = Foo('Bar')
print(foo.name) 