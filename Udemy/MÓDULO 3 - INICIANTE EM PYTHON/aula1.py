print(12, 34) # argumento não nomeado
''' 
DocString
joga coisas na tela e requisita um argumento
CTRL + C e CTRL + V copia e cola a linha sem precisa selecionar

\r \n -> CRLF 

quebra de linha e retorno
'''

print(12, 34, sep='-')# separador (coloca um tracino no espaço da vígula)
print(12, 34, end='##') # terminador
print(56, 78)
print(12, 34, flush=True) # limpa a tela
print(12, 34, sep='-', end='-', file=open('arquivo.txt', 'a')) # arquivo
'''-------------------------------------------------------------------------------------'''
# Aula de tipagens, dinamica (sabe interpretar sozinho) e forte
'''
str -> String
int -> Integer (numero inteiro)
float -> Float (real)
bool -> Booleano  (True e False)

tipos primitivos para tipagem

a função type retorna  uma classe (um objeto) com o tipo do valor 
booleano operador para "questionar o programa" 
'''

print(type(12)) #Integer
print(type("Douze")) # String
print(type(12.34)) #Float 
print(type(True)) #Boolean 
print(type(False)) #Boolean
print(type(None)) #NoneType

'''-------------------------------------------------------------------------------------'''
print(100==100) #Booleano que retorna True
print(12==113) #Booleano que vai retorna False