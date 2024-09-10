'''
Métodos úteis dos dicionários em Python

(não especificamente é um metodo)len - quantas chaves
keys - iteráveis com as chaves
values - iteráveis com os valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave especificada(del)
popitem - apaga o ultimo item adicionado
update - atualiza um dicionario novo
'''
pessoa={
    'nome' : 'Lucas',
    'idade': 18,
    'sobrenome' : 'Meleti',
    'date' : 18.05
}
print(len(pessoa)) 
#print em quantas chaves existem nesse objeto

print(pessoa.keys()) 
#retorna as chaves disponíveis em um dict_keys, mas isso pode ser convertido para Tuple ou List caso queira
print('\n',list(pessoa.keys()))

print (list(pessoa.values()))
#Keys retorna as chaves e Values retorna cada valor destas chaves


print('\n', list(pessoa.items()))
#retorna chaves e valores juntos
# retorna lista com tuplas (MUITO parecido com o caso do enumerate, pois retorna o index(chave) e o valor)

print('\n', pessoa.setdefault('data', None))
#usado para tratamento do erro, setdefoult deixa como padrão um valor para o caso da variável não existir
#caso essa variável exista, ele deixa de usar este valor padrão 

#-------------------------------------------------------------------------------

#lembre-se que são mutáveis
import copy
d1 = {
    'c1' : 1,
    'c2' : 2
}
d3 = {
    'c1' : 1,
    'c2' : 2,
    'l1' : [1,2,3,4,5]   
}
# d2 = d1 ESTÁ ERRADO. Isso indica que d2 aponta para o mesmo dicionário de d1, e não que ele recebe
# para isso temos o método copy, que de fato copia o dicionario para o lugar indicado  
d2 = d1.copy()
# CONTUDO , foi uma copia rasa, pois copiou apenas os valores imutáveis
# por exemplo isso não copia listas. os valores mutáveis apontam para a mesma memória

# Para copiar bonitinho, use o import copy , e depois deepcopy
d2 = copy.deepcopy(d3)
d2['l1'][1] = 10000
d3['l1'][1] = 18
print(d2,d3)

#-------------------------------------------------------------------------------

print(pessoa.get('nome'))
#Retorna o valor da chave e retorna None caso não haja, isso evita alguns erros e também retorna o valor

nome = d1.pop('c1')
#Assim como na lista, você remove o valor indicado do dicionário e retorna esse valor 
print(nome)
print(d1)

ultima_chave = pessoa.popitem()
# Remove e retorna o ultimo valor e chave do dicionário em uma tuple
print(ultima_chave)
print(pessoa)

#-------------------------------------------------------------------------------

pessoa.update({
    'date' : 18.05,
    'idade' : 19
}) # update atualiza chaves já existentes e cria novas caso precise

# pessoa.update(idade = 19, date = 18.05) outra forma de escrever
#update TAMBÉM funciona com listas e tuplas que se comportam como dicionários
