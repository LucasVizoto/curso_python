'''
função lambda em Python

essa função lambda é uma função como qualquer outra em Python. Porém, são funções 
anônimas que contém apenas uma linha. Ou seja, tudo deve ser contido de 
uma unica expressão

lista = [
    {'nome':'Lucas', 'sobrenome' : 'Meleti'}
    {'nome': 'Beatriz', 'sobrenome' : 'Vizoto'}
]

    ARROW FUNCTION
'''
lista = [1,54,18,5,34,565,345,23,4,31]
lista.sort() #organiza a lista em ordem crescente
print(lista)
lista.sort(reverse=True) # decrescente
lista2 = sorted(lista) #sorted retorna o valor analisado

#----------------------------------------------------------------

#Python não faz sort de dicionário, por isso
lista = [
    {'nome':'Lucas', 'sobrenome' : 'Meleti'},
    {'nome': 'Beatriz', 'sobrenome' : 'Vizoto'},
    {'nome': 'Gabriel', 'sobrenome' : 'Assed'},
    {'nome': 'Augusto', 'sobrenome' : 'Benate'}

]

nome = sorted(lista, key=lambda item: item['nome']) #vai funcionar como um some
sobrenome = sorted(lista, key=lambda item: item['sobrenome']) #vai funcionar como um some
#sorted faz cópia rasa
'''
def ordena(item):
    return item['nome']

lista.sort(key=ordena)    
'''

for item in lista: 
    print(item)