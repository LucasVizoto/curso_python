texto = 'Python'

i=0
tamanho_string = len(texto)

while i < tamanho_string:
    print(texto[i])

    i += 1

#----------------------------------------------------------------
texto_2 = 'Python'
novo_texto = ''
for letra in texto_2:  #Para cada letra em texto 
    novo_texto += f'{letra}' 
    print(letra)       # Lembra muito o forEach, letra é o indice [i]
    print(novo_texto) #Concatena a frase
# iterável entrega um valor ppor vez, uma String é iterável
# While é usado para coisas que não sabemos o tamanho (Solicitação de uma senha)
# Enquando o for é usado para coisas quesabemos o tamanho

#----------------------------------------------------------------
'''
range -> range(starr,stop,step)
usado em números
'''
numeros = range(10) #Numeros de 0 a 10
numeros = range(5,10) #Numeros de 5 a 10
numeros = range(0,10,2) #Numeros de 0 a 10 indo de 2 em 2 
#Lembrando que não conta o último valor

for valor in  numeros:
    print(valor)

x = valor*5
for valor_2 in range(0,10): # in range seria como se fosse um (let *i=0*, *i++*) a condição entre os i seria o valor atribuido antes do in
    valor_2 += x+1    
    print(valor_2)
#----------------------------------------------------------------
'''
Como o for funciona?

Iterável - >  str, range, etc (tem o método ___iter___ dentro dele) iterável entrega um valor ppor vez
iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor disponível no iter
iter - > me entregue seu iterador  (diz onde está o iterador na memória. Lembra muito o ID)

quando você sai pra comprar gás, o vendedor precisa ligar pra saber se tm gás
então ele vai no iter para o conversar com o iterador

iter() (função) é a mesma coisa que chamar o método .__iter__ (dunder são os underlines)
next() (função) também é a mesma coisa que .__next__()
método = .
função = () 
'''
texto = iter('Lucas') #.__iter__
print(texto) 
print(texto.__next__()) # vai imprimir L
#----------------------------------------------------------------
#for item in texto (forEach)
texto = "Lucas"
iterador = iter(texto) 

while True:
    try:
        print(next(iterador))
    except StopIteration: # Quando der o erro StopIterator, vai parar
        break 
# Esse erro é forçado pelo for (Ele é executado exatamente como o código acima)

for letra in texto:
    print(letra) #É literalmente a mesma coisa
#----------------------------------------------------------------
'''
As coisas do while também também se enquadram no for
continue, break, else

# for(i=0;i<9;i++){} é a mesma coisa do de baixo
for i in range(10):
    if i == 5:
        print('i é igual a 5... Pulando pq está no Continue')
        continue
    
    if i ==8:
    print('i é igual a 8, seu else não vai executar')
    break
    
    for j in range(1,3):
        print(i,j)
else:
    print('For Completo com Sucesso')

    LEMBRANDO: o else de While e for só executam se esses não tiveram um break
    e se executaram normalmente do inicio ao fim
'''