'''
É BASICAMENTE UM OBJ DE JAVASCRIPT
Dicionários em Python (tipo dict)
 Dicionários são estruturas de dados do tipo
 par de "chave" e "valor".
 Chaves podem ser consideradas como o "índice"
 que vimos na lista e podem ser de tipos imutáveis
 como: str, int, float, bool, tuple, etc.
 O valor pode ser de qualquer tipo, incluindo outro
 dicionário.
 Usamos as chaves - {} - ou a classe dict para criar
 dicionários.
 Imutáveis: str, int, float, bool, tuple
 Mutável: dict, list
 pessoa = {
     'nome': 'Luiz Otávio',
     'sobrenome': 'Miranda',
     'idade': 18,
     'altura': 1.8,
     'endereços': [
         {'rua': 'tal tal', 'número': 123},
         {'rua': 'outra rua', 'número': 321},
     ]
 }
 pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda') função com dict(também cria um objeto mas dessa forma)

 .get = usado para tratamento de erro para caso uma chave não exista
 '''
#usados para coisas com atributos

pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'Meleti',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
         {'rua': 'tal tal', 'número': 123},
         {'rua': 'outra rua', 'número': 321}
     ] #no endereço tem uma array com endereços
}
print (pessoa, type(pessoa)) #Vai retornar um dict por ser um dicionario

print(pessoa['nome'])
print(pessoa['sobrenome'])

for chave in pessoa:
    print(chave, pessoa[chave])
#------------------------------------------------------------------------
produto = {}
produto['alimento'] = 'Arroz'
#Colocando uma chave inexistente e atribuindo valor a ela, voce consegue adicionar uma nova chave ao dicionario/obj
#Coloocar uma chave inexistente gear uma KeyError
produto['nome'] = 'Lucas'

del produto['nome'] #deletar chaves
#A função get consegue fazer uma comparação se a chave existe ou não

if produto.get('nome') is None: #Vai retornar None se não existir, e retorna o valor se existir
    print('NÃO EXISTE')
else:
    print(produto['nome'])

print(pessoa.keys())
print(pessoa.values())

for chave, valor in pessoa.items():
    print(chave, valor)

