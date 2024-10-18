# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# min max = funções úteis que podem facilitar e muito a tua vida


lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

# def lista_maior(lista1, lista2):
#     if len(lista1) > len(lista2):
#         return lista1
#     else:
#         return lista2

def zipper(lista1, lista2):
    intervalo_máximo = min(len(lista1),len(lista2)) #Qual o menor len das duas listas
    return [
        (lista1[i], lista2[i]) for i in range(intervalo_máximo)
    ]
lista_zipada = zipper(lista1, lista2)

print(lista_zipada)

# PODE SER FEITO TAMBÉM USANDO A FUNÇÃO ZIP (retornqa um iterator)
print(list(zip(lista1, lista2)))


# lista_numeros = [1,2,3,4,5,6,7,8,9,10,11]
# print(max(lista_numeros)) #maior número da lista
# print(min(lista_numeros))# menor número da lista