# Combinação, Permutation e Product - itertools
# combinação - Ordem não Importa - Iterável + tamanho do grupo
# Permutação - Ordem Importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product
from pprint import pprint
pessoas = ['João', 'Joana', 'Luiz', 'Letícia']
camiseta = [
    ['preto', 'branca'],
    ['p','m','g'],
]

pprint(list(combinations(pessoas, 2))) #passa-se a lista e a quantidade de itens no grupo
# combinations não repete valores, diferente da Permutation
print()

pprint(list(permutations(pessoas, 2))) #Junta, todas as combinações de dados dentro da lista
print()

pprint(list(product(*camiseta))) #Numa lista de tuplas ele gera combinações de duas listas dentro dele
# neste caso combinações com as cores e tamanhos listados na lista camisetas
# gera um crescimento exponencial

lista_compras = [
    ['preta', 'jeans','bege'],
    ['p','m','g','gg']
    ['masculina', 'feminina']
    ['algodão', 'poliéster']
]
pprint = (product(*lista_compras))