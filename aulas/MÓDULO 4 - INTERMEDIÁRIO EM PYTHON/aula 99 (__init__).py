'''
__init__ é sempre executado quando você importa o package
pois normalmente, importar o package não resulta em nada, se não chamar o module

VOCÊ FAZ O PYTHON ACREDITAR QUE ISSO É UM MÓDULO
'''
import aula99_package

from aula99_package import soma

print(soma(2))