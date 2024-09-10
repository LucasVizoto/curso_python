# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
# SERIA POSSIVEL CRIAR UM MÓDULO NA QUAL RECEBERIA ESSE VETOR COM PRODUTOS
# MAS EU PARTICULARMENTE PREFIRO DEIXAR AQUI PARA ENTENDER DEPOIS
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
import copy
import pprint #imprime bonitinho


novos_produtos = [
    {**p, 'preco' : round(p['preco']*1.1, 2)}
    for p in copy.deepcopy(produtos)
                  
# faz uma deep copy e altera apenas o número que está aqui, Com isso, da pra
# alterar o valor para usando a chave para pegar o valor requisitado
# round é para arredondar
]

pprint.pprint(novos_produtos)

ordem_produtos_crescente = sorted(copy.deepcopy(produtos), key=lambda p: p['preco']) 
pprint.pprint(ordem_produtos_crescente)

ordem_produtos_por_nome = sorted(copy.deepcopy(produtos), key=lambda p: p['nome']) 

#sorted faz cópia rasa e retorna o valor analisado