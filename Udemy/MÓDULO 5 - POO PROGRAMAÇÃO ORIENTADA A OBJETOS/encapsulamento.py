# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#     (sem underline) = public
#         pode ser usado em qualquer lugar
#     (um underline _ ) = protected
#         NÃO DEVE ser usado de fora da classe 
#         ou suas subclasses
#     (dois underlines __ ) = private
#         'name mangling' (desfiguração de nomes) em Python
#         SÓ DEVE ser usado na classe em que foi declarado
        # SÓ PODE SER USADO ONDE ELE FOI DEFINIDO

# a POO tem 4 pilares, sendo eles: Encapsulamento, Polimorfismo, Abstração e Herança
from functools import partial



class Foo:
    def __init__(self):
        self.public = 'Isso é público'
        self._protected = 'Isso é protegido'
        self.__private = 'Isso é privado apenas dessa classe'
        self._metodo_protected() #aqui nn é errado

    def metodo_publico(self):
        return 'metodo_publico'    
    
    def _metodo_protected(self):
        return '_metodo_protegido'
    def __metodo_private(self):
        return '__metodo_privado'
f = Foo()
print(f.public)         
print(f.metodo_publico)

print(f._metodo_protected) # NÃO SE DEVE FAZER ISSO, POR MAIS QUE FUNCIONE, 
# A CONVENÇÃO DIZ QUE O _ INDICA PROTEÇÃO E QUE ISSO NÃO DEVE SER FEITO