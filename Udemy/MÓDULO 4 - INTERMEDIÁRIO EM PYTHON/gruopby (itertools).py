from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def ordena_dicionário():
    return sorted(alunos, key=lambda x: x['nota'])
# sorted agrupa e ordena a lista, MAS, no caso de dicionário é necessario uma Key
# foi passado essa key para uma lambda, gerando uma nova função onde a é a chave 
# principal puxando nota 
# lembrando que, por mais que sorted ordene ele retorna uma shallow copy



# alunos_novos = ['a','a','a','b','c']

# grupos = groupby(alunos_novos)

# for chave, grupo in grupos:
#     print(chave)
#     print(list(grupo))
#     print(grupo)

# groupby é basicamente um agrupamento de valores, se você esquecer de ordenar,
# ele criará um novo conjunto
alunos_agrupados = ordena_dicionário()
grupos = groupby(alunos_agrupados, key = lambda x: x['nota'])

for chave, grupo in grupos:
    print(chave)
    print(list(grupo))
    print(grupo)