# Herança simples - Relações entre classes
# associação - um obj USA outro obj 
# Agregação -  um obj TEM outro obj
# Composição - é dono de

# herança - É um

# Herança ou Composição

# Classe principal(Pessoa)
#  chamo de (hieraquicamente acima)-> super class, base class, parent class

# Classes filhas(Cliente)
#  chamo de -> sub class, child class, derived class

# cliente herda de pessoa por herança, extende

# o cliente é do tipo pessoa, uma classe é outra
# cliente pela herança é uma pessoa

# sua classe já recebe uma herança da classe object do built in que vem por padrão no python


class heranca(object):
     ...
# Isso é um exemplo de herança pois uma classe recebe como 'parametro' outra
# em outras linguagens você usa extends


class Foo:
    ...
# help(Foo)

class Pessoa:
    def __init__(self, nome, sobrenome):
          self.nome = nome
          self.sobrenome = sobrenome
    def falar_nome_class(self):
         print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
#todo o código que já havia em pessoa, vem automaticamente para cliente 
    ... 

class Aluno(Pessoa):
     ...

c1 = Cliente('Lucas', 'Meleti')
c1.falar_nome_class()
a1 = Aluno('Beatriz', 'Vizoto')

#Method resolution order - MRO (Quando você chamar um método, a ordem exibida é a que ele vai fazer)
# Colocar no máximo três itens pra não ficar muito complexo