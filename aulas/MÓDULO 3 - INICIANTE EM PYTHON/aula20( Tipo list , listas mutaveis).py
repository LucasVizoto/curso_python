'''
Lista em Python
Tipo list - Mutável (array)
Suporta vários valores de qualquer tipo
Conhecimentos Reutilizaveis - índices e fatiamento

Métodos Úteis =: 
        append, insert, pop, del, clear, extend, +
        create, read, update, delete
        criar,  ler,  alterar, apagar = lista[i] (CRUD)


tipo list é literalmente um VETOR


#----------------------------------------------------------------
    
    append - Adiciona um item ao final
    insert - Adiciona um item no indice desejado
    pop - Remove o último item da lista ou item escolhido e retorna o valor
    del - apaga um indice
    clear - Limpa a lista
    extend - estende a lista (concatena na lista referenciada)(não retorna valor)
    + - Concatena duas listas

#-----------------------------------------------------------------    
'''
#         01234
string = 'ABCDE' #5 caracteres (len) 

lista = list() #Se quer converter dados em uma lista
# OU 
lista_comum = [] # lista vazia
# se uma lista vazia é confrontada com um booleano, ela é False
print(bool(lista_comum))
print(lista_comum, type(lista_comum)) #type informa o tipo do Dado

lista2 = [123, True, 'Lucas Vizoto', 1.2 ,18.05, 2023, 1324,34, 265,87]
print(lista2[2].upper(), type(lista2[2])) #LUCAS VIZOTO <class 'str'>
lista2[2] = 'Bia'
print(lista2[2])

#----------------------------------------------------------------

del lista2[1] # Vai APAGAR o valor no indice referido, literalmente dá um delete
# o lista2[1] agora é 'Bia' e o vetor só tem 4 de length agora

lista2.append(18.05) #Adiciona no final da lista
# Tipo um .push

lista2.append(2023)

lista2.pop() # retira o último item da lista até esse momento
#pop, além de remover o valor, ele rouba pra ele. Em breves palavras, o return dele é o valor removido
ultimo_valor = lista2.pop()
print(ultimo_valor)
#os parametros do pop podem também ser o indice do item que deseja retirar
lista2.pop(7) #removeu o item 7

#----------------------------------------------------------------

lista3 = [1,2,3,4,5,6,7,8,9,10]
lista3.clear() #limpa tudo
print(lista3)
#------------------------------
lista4 = [1,2,3,4,5,6,7,8,9,10]
lista4.insert(0, 'Pessoa') #informa o indice primeiro e depois o valor a ser adicionado
#Se o número passar do indice no insert ele coloca no final
# lista4.insert(18000, 05) #Vai colocar depois do 10
#------------------------------
# Se você tentar colocar um valor num index inexistente, ele irá retornar um IndexError
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
print(lista_c)

lista_d = lista_a.extend(lista_b) #Vai retornar um None (Sem valor) pois como dito em cima ele não retorna valores e sim concatena na lista_a

lista_a.extend(lista_b)
print(lista_a)

#----------------------------------------------------------------

lista_a = lista_b #Ambos apontando pro mesmo valor na memória, uma não recebe a outra
# se for altaredo qualquer uma das duas, ambas sofrerão a alteração
lista_a = lista_b.copy() #Vai copiar a lista para dentro da outra, resolvendo o problema