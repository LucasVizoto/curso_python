frase = 'O Python é uma linguagem de programação '\
        'multiparadigma' \
        'Python foi criado por Guido van Rossum.'
# barra invertoida quebra o código (shift + enter)

print(frase.count('Python')) #retorna quantas vezes apareceu Python na frase

i = 0
letra_com_mais_caracteres = " "
numero_de_vezes_que_apareceu = 0
while i<len(frase):
    letra_atual = frase[i]
    qtdd_atual = frase.count(letra_atual) #Vai imprimir a quantidade de letras que apareceu em cada caractere
    if letra_atual == ' ':
        i += 1 #Mais pq o i bugaria o código
        continue #Continue volta pro inicio do laço, logo, ele vai ignorar os Espaços 
    if qtdd_atual > numero_de_vezes_que_apareceu:
        numero_de_vezes_que_apareceu = qtdd_atual
        letra_com_mais_caracteres = letra_atual
    print(letra_atual)
    i +=  1
# Iterar é escrever a frase dessa forma(iterar a String)

print(f'O caractere que maios apareceu é o :  {letra_com_mais_caracteres} \n' \
      f'A quantidade de vezes que apareceu é : {numero_de_vezes_que_apareceu}')
