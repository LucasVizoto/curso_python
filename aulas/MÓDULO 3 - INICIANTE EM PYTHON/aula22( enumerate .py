#enumerate - enumera listas iteráveis (contar o i )
lista = ['Lucas', 'Beatriz', 'Camilo', 'Luis']
lista.append('Gabriel')

lista_enumerada = enumerate(lista) #iterator
print(lista_enumerada) # retorna o id de memória + enumerate
print(next(lista_enumerada))#próximo valor 
# enumerate vai retornar uma Tuple()
# Retorna o indice e o valor atrelado a esse índice,
# EX.:
#  
# 0, Lucas
# 1, Beatriz
# 2,Camilo   

for item in lista_enumerada:
    print(item)
for item in lista_enumerada: # Não acontece nada pq foi consumido
    print(item)
for item in lista_enumerada: # Não acontece nada pq foi consumido
    print(item)    
#Você só pode usar uma vez o enumerate, pois ele é consuimido durante o uso
# O certo é utilizar o enumerate no for, pois assima sempre se está criando um novo e reestartando a contagem

for item in enumerate(lista):
    print(item)
for item in enumerate(lista):
    print(item)
for item in enumerate(lista):
    print(item)

enumerate(lista, start = 10) #Começa no valor de indice indicado 

# Para converter em lista o enumerate, basta usar o list() ou tuple() para tupla
# Vetor com tuplas dentro
# [(indice, valor), (indice, valor), (indice, valor)] = [(0, Lucas), (1, Beatriz), ...] 

lista_enumerada = list(enumerate(lista))
print (lista_enumerada)

# Como é uma tupla basta desempacotar 

for indice, nome in enumerate(lista): #Desempacota sozinho
    print(indice, nome) 
    print(f'\t{indice}') #\t da tab 