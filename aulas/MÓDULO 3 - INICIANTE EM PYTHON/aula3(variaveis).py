# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minúsculas, pode usar
# números e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para
# atribuir um valor a um nome (variável).
# Uso: nome_variavel = expressão (Snake Case, separa espaços nas variáveis com undeline)

# nome_completo = 'Lucas Vizoto'
# soma_dois_mais_dois = 2 + 2
# int_um = int('1')
# print(int_um, type(int_um))
# print(nome_completo, soma_dois_mais_dois)

#  EXERCICIO
idade = input('Digite a idade do indiviiduo: ')
maior_de_idade = idade>=18 #Funciona como uma espécia de IF dentro da variável

print('é maior de idade? ', maior_de_idade) #retorna uma booleana Falsa caso o valor digitado não satisfaça a condição

'''---------------------------------------------------'''

print('Divisão', 10/2.2) 
print('Divisão Inteira', 10/2.2) #Retira a parte decimal

'''---------------------------------------------------'''

nome = "Lucas"
sobrenome = "Vizoto"
print(nome+sobrenome) #Vai concatenar os valores enviados
print(nome*3) #Vai repetir 3 vezes a variável nome no print