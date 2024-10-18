import json

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    # tuplas quando passadas para Json viram uma array e votam como list
    'dev': True,
    'nada': None,
}

with open('aula_json.json', 'w') as arquivo:
    json.dump(pessoa, arquivo, indent = 2) #faz um dump num arquivo ()
# cria um json com todas as informações do dicionário informado
with open('aula_json.json', 'r', encoding='utf8') as arquivo:
    pessoa_de_novo = json.load(arquivo)    
# carrega no terminal as informações do Json
print(pessoa_de_novo['nome'])