'''
split e join com list e String

split - divide uma String
join - une uma String
'''

frase = 'Olha que, bagulho foda'
lista_palavras_crua = frase.split() #Vai dividir a String nos espaços em branco se não tiver nada
#O parametro é para mostrar o caractere que possui carater divisor na string
# retorna um array
print(lista_palavras_crua) #
lista_2 = frase.split(',') # Vai separa na vírgula evai criar uma lista de frases

for i, frase in enumerate(lista_palavras_crua):
    print(lista_palavras_crua[i])
    print(lista_palavras_crua[i].strip()) #Strip corta os espaços sobrando da String (esquerda e direita)
    print('\n',lista_palavras_crua[i].lstrip()) #corta da left
    print(lista_palavras_crua[i].rstrip()) # corta da right
#----------------------------------------------------------------
lista_frases_formatada = []
for i, frase in enumerate(lista_palavras_crua):
    lista_frases_formatada.append = lista_palavras_crua[i].strip()
    print(lista_frases_formatada)
#----------------------------------------------------------------
frases_unidas = '-'.join('abc') #Vai unir ops valores colocados 
# Essa String é o valor que irá separar as frases
print(frases_unidas)

frases_unidas = '-'.join(frase)