'''
d - int
f - float
.(nº de dígitos)f 
Caractere ><^ quantidade
 0 > - 100,.1f
 > - Esquerda
 < - Direita
 ^ - Centro
 sinal - + 
 conversion Flags - !r !s !a
 pad - preenche com uma quantidade definida de caracteres, caso não tenha
 o length solicitado
'''
variavel = 'abc'
print(f'{variavel: >10}. ') # Joga os caracteres para a Esquerda
print(f'{variavel: <10}. ') # Joga a Direita
print(f'{variavel: ^10}. ') # Joga para o Centro
# O valor antes do sinal é o que vai ser colocado no lugar
# print(f'{variavel: %^10}') = %%%abc%%%%

#=-----------------------------------------------

'''
Fatiamento de Strings
012345678
Olá Mundo

Fatiamento [i:f:p] [::]

inicio, fim, passo (vai contar de quanto em quanto)
a funcao len retorna a qtdd de Caracteres da str
'''
variavel = 'Olá Mundo'
print(variavel[4:]) #do indice 4 até o fim (fim pq nn tem nada)
# mesma coisa que print(variavel [4:f])
# : -> indica que é pra fazer o fatiamento
print(variavel[4:8]) # = mund (mesmo o d sendo do indice 7 o python não considera o final, então tem que jogar um a mais)
print(variavel [:5]) # Se não tiver nada ele considera inicio ou fim

print(len(variavel)) #Checa o tamanho da string, MAS conta o zero como um
# Olá Mundo tem 8 de indice mas tem 9 de len

print(variavel[0: len(variavel): 1 ]) # vai do inicio ao fim andando de 1 em 1
print(variavel[::-1]) #Como não tem nada considera inicio e fim, MAS, por estar negativo, ele anda ao contrário
