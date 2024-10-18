cont = 0
nome_pessoa = input('Digite seu nome: ')
while cont<len(nome_pessoa):
    print(nome_pessoa[cont], end='\n')
    cont += 1
# **= (Potencia) 
#  /= (divide o que tem)
#  //= (divide inteiro)
#  %= (Módulo)   
variavel = 0
while True:
    variavel += 1
    print(variavel)
    break # Break quebra o laço

contador=0

while contador<=100:
    contador += 1

    if contador == 6:
        continue # Continue faz o contador parar e voltar ao inicio do laço (não mostra o 6)
    if contador >=10 and contador <=27:
        continue # Continue faz o contador parar e voltar ao inicio do laço (não mostra do 10 ao 27)
    print(contador, end='\n')
    if contador == 50:
        break # Break quebra o laço