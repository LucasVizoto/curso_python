# Herança multipla - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender
# várias outras classes

# Herança Simples:
# Animal -> Mamífrero - > Humano -> Pessoa -> Cliente
# herança multipla e mixins

# Log -> Filelog
# Animal -> Mamífrero - > Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog) | puxa a herança dos dois pontos

# A, B, C, D
# D(B,C) - C(A) - B(A) - A
# método -> falar
#             A
#           /   \
#          B     C
#           \   / 
#             D
# problema do diamante - Fazer isso pode arruinar seu programa

# python 3 usa C3 superclass linearization
# para gerar o mro 

# Para saber a ordem de chamada dos métodos 
# Use o método de classe NomeDaClasse.mro()
# ou o atributo __mro__

# herança múltipla pode ser o sucesso do seu programa, ou pode ser a ruína
# tome nota: Passou de 3 heranças fica paia

class A:
    def falar(self):
        print('A')

class B(A):
    def falar(self):
        print('B')

class C(A):
    def falar(self):
        print('C')
#o mro da herança segue essa sequencia que foi passada nos parâmetros
class D(B, C):
    def falar(self):
        print('D')

d = D()
d.falar()

print(D.mro())