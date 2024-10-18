'''
Sets - Conjuntos (da matemática) em Python (tipo set)
Conjuntos são ensinados na matemática
https://brasilescola.uol.com.br/matematica/conjunto.htm
Representados graficamente pelo diagrama de Venn
Sets em Python são mutáveis, porém aceitam apenas
tipos imutáveis como valor interno.

Criando um set''' 

#set(iterável) ou {1, 2, 3}
s1 = set('Lucas')
s1 = set()  #vazio
print(s1) # retorna algarismos separados fora de ordem ou na ordem
s1 = {'Lucas', 1, 2, 3}  #com dados
print(s1)

# o set vai iterar a respeito doq foi colocado de parâmetro

'''
Sets são eficientes para remover valores duplicados
de iteráveis.
- Não aceitam valores mutáveis;
- Seus valores serão sempre únicos; (tira os repetidos)
- não tem índexes;
- não garantem ordem;
- são iteráveis (for, in, not in)
'''
s2 = {1,2,3,3,3,3,2,4,5,6}
print(s2) 
#tirou os repetidos
# EX.:
l1 = [1,2,3,3,3,3,2,4,5,1]
s3 = set(l1)
l2 = list(s3)
print(l2) #o set limpou os repetidos e mandou a sim
#aceitam (for, in, not in)

'''
Métodos úteis:
add, update, clear, discard
'''
seto = set()
seto.add('Lucas')
seto.add(1) # .add adiciona o valor do parâmetro nesse conjunto
#só pode um valor por vez
print(seto)

seto.update('Hello World!') # .update também coloca, mas coloca letra por letra
# OU
seto.update(('Hello World!',1,2,3,4))
#Passar uma tupla com todos os valores

#seto.clear() limpa o set (por isso está comentado ksksk)

seto.discard('Hello World!')
#como um set nn possui indice, para vc apagar um valor, você precisa passar o próprio valor
print(seto)

#----------------------------------------------------------------

'''
Operadores úteis:
união | união (union) OU - Une
intersecção & (intersection) E - Itens presentes em ambos
diferença - Itens presentes apenas no set da esquerda
diferença simétrica ^ - Itens que não estão em ambos
'''
b1 = {1,2,3}
b2 = {2,3,4}

l3 = b1 | b2 #junta os dois em um só
l4 = b1 & b2 #mostra o que tem nos dois conjuntos em comum
l5 = b1 - b2 #Vai retornar o valor que só tem em b1
l6 = b1 ^ b2 #Item único de cada um dos conjuntos (1, 4)


#----------------------------------------------------------------

#exemplo de uso de Tipo set

letras = set()
while True:
    caractere = input('Digite: ')
    letras.add(caractere.lower())

    if 'l' in caractere:
        print('PARABÉNS')
        break
# set() é útil por causa da não repetição dos itens   