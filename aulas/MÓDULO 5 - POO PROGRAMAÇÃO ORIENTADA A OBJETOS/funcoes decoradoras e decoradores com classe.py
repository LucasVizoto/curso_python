def adiciona_repr(cls):
# cls representa que se deve passar uma classe
    def funcao_repr(self): #funciona COMO se estivesse em uma classe
        class_name = self.__class__.__name__
        class_dict = self.__class__.__dict__
        class_repr = f'{class_name} {class_dict}'
        return class_repr
    cls.__repr__ = funcao_repr # no dunder repr da classe, insere a function
    return cls #devolve pra classe
#função dentro de outra

def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)


        if 'Terra' in resultado:
            return 'Você está em casa'

        return resultado
    return interno

class MyReprMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__class__.__dict__
        class_repr = f'{class_name} {class_dict}'
        return class_repr
#se não setar o repr aparece o id, isso é para ser padrão e conseguir passar
# o mesmo repr pra todas as classes

@adiciona_repr #classe foi decorada
class Time:
    def __init__(self,nome):
        self.nome = nome

@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def falar_nome(self):
        return f'O planeta é {self.nome}'

brasil = Time('Brasil')
portugal = Time('Portugal')


terra = Planeta('Terra')
marte  = Planeta('Marte')

print(brasil)
print(portugal)


print(terra)
print(marte)

print(terra.falar_nome())
print(marte.falar_nome())