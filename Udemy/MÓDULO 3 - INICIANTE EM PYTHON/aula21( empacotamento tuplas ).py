lista = ['Lucas', 'Beatriz', 'Camilo', 'Luis']

#Desempacotamento, tirar coisas dos campos
# VocÊ pode criar variaveis com os e colocar estas recebendo a lista

nome1, nome2, nome3, nome4 = lista
print(nome1,nome2)
#----------------------------------------------------------------
# Se colocar mais variaveis doq valores, ou o contrário, tbm da erro
# Se quiser pegar valores específicos, voce pode colocar a variavel *resto
#O resto vai gerar um array com os demais itens que não foram usados

nome1, *resto = lista #resto é o nome da variável
print(nome1, resto)
# Não tem como só separar um valor além do primeiro e jogar o resto no array de resto

#-----------------------------------------------------------------
#tupla é uma lista imutável

lista2 = 'Lucas', 'Beatriz', 'Camilo', 'Luis'
print(lista2[1])
print(lista2)

tuple(lista) #converte para tupla
list (lista) #converte para lista
