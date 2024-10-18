from functools import partial
from types import GeneratorType
#functool é uma biblioteca para funções
# patial é uma função que recebe uma função um ou varios argumentos


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Notebook', 'preco': 2000},
    {'nome': 'Tablet', 'preco': 1000},
    {'nome': 'Mouse', 'preco': 500},
    {'nome': 'joystick', 'preco': 900},
    {'nome': 'Produto_Final', 'preco': 1001}
]

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem)
aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem = 1.1)


    # novos_produtos = [{**p, 'preco': aumentar_dez_porcento} for p in produtos ]
    # print_iter(produtos)

def muda_preco_de_produtos(produtos):
    return {**produtos, 'preco': aumentar_dez_porcento(produtos['preco'])}


novos_produtos = map(muda_preco_de_produtos, produtos)
# map vai passar a função em cada um dos produtos
# MAP É UM ITERATOR

print_iter(novos_produtos)
print(isinstance(novos_produtos,GeneratorType))
#verifica se o item passado é um generator ou não, vai retornar False


print(list(map(lambda x: x*3, [1,2,3,4,5,6,7,8,9])))

# primeiro vem oq você vai fazer com seu mapeamento, e depois o objeto que vai
# ser mapeado


'''
map é uma função que recebe uma função e um iterable
map retorna uma nova lista com os resultados da função aplicada a cada elemento do iterable
'''



#-------------------------------------------------------------------------------------------------------------------

# FILTER
# SE FOR IGUAL AO DO JS, CRAI UMA NOVA LISTA COM OS ITENS INDICADOS

produtos_diferentes = [p for p in produtos if p['preco'] > 1000]
# você filtra o valor com base em argummentos
# list comprehension
produtos_diferentes_filtered = filter(lambda p: p['preco'] > 1000, produtos)
# na função filter, o primeiro parâmetro sempre será uma função e o segundo um iterável
# se ao invés de usar uma lambda, vc decidir passar uma função já feita,
# lembre-se que ela não será executada, logo, NÃO USE PARENTESES

# produtos_diferentes_filtered = filter(funcao_que_faz_o_bagulho, produtos)


print_iter(produtos_diferentes)
print_iter(produtos_diferentes_filtered)
