# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
import sys
        #   sys.exit()#Sai do programa

# precisa usar o name space (sys, random, time)

# platform = 'A MINHA'
# print(sys.platform)
# print(platform)


#Para importar uma parte de um módulo 
# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
from sys import exit, platform
print(platform)


# alias 1 - import nome_modulo as apelido
import sys as s # import sys como s (Quase NUNCA faça isso, dificulta documentação)
sys = 'alguma coisa'
print(s.platform)
print(sys)
# Platform mostra a plataforma que está rodando

# alias 2 - from nome_modulo import objeto as apelido
# from sys import exit as ex
# from sys import platform as pf

# print(pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

#      má prática - from nome_modulo import * (importa TUDO)
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo
# from sys import exit, platform

# print(platform)
# exit()