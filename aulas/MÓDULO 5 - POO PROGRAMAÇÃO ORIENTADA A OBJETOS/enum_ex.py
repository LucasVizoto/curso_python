# Enum -> Enumerações
# enumeração de coisas
# tem uma chave e enumeração

from enum import Enum
from shutil import move

class Status(Enum):
    ATIVO = 1
    INATIVO = 2
    BLOQUEADO = 3

# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para ESCOLHER.
# Enums têm membros e seus valores são CONSTANTES.
# Enum é uma classe mas não se comporta como classe, seus membros são sua enumeração

# como no exemplo acima ounde os status são definidos com os numero 1 2 e 3
#
# 
#      
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a SUPERCLASS para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:

# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value

def mover(direcao):
    if direcao not in ['esquerda', 'direita', 'cima', 'baixo']:
        raise ValueError(f'Direção inválida: {direcao}')
    
     # aqui é uma abstração
    print(f'Movendo para {direcao}')

mover('esquerda')
mover('direita')
mover('cima')
mover('baixo')

# Isso pode ser substituido por

# from enum import Enum
Direcoes_JEITO_ESTRANHO = Enum('Direcoes', ['ESQUERDA', 'DIREITA'])

class Direcoes(Enum):
    ESQUERDA = 1
    DIREITA = 2
    CIMA = 3
    BAIXO = 4 
    # caso você não ligue para a numeração vocÊ pode usar um enum.auto()

print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.DIREITA)
print(Direcoes(1).name, Direcoes.ESQUERDA.value)


def mover_com_Enum(direcao : Direcoes): #aqui você aponta o tipo dessa funçao
    if not isinstance(direcao, Direcoes):
        raise ValueError(f'Direção inválida: {direcao}')
    
     # aqui é uma abstração
    print(f'Movendo para {direcao.name} ({direcao.value})')

mover(Direcoes.DIREITA)
mover(Direcoes.ESQUERDA)
mover(Direcoes.CIMA)
mover(Direcoes.BAIXO)
