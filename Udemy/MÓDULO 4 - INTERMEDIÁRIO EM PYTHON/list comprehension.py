# lis comprehension é uma forma rápida para criar listas a partir de iteráveis

lista = [1,2,3,4,5,6,7,8,9,10]
lista_completa = [x*x for x in lista]
lista_com = [lista.append(numero) for numero in range(10)]
# criação automática de uma lista usando o ternário do for
#[código a ser executado da lista for item in condição]
print(lista_completa)

lista_nova = [numero*2 for numero in range(10)]
print(lista_nova)

#----------------------------------------------------------------