'''
While/else 
executa um else se percorrer o While todo corretamente (sem usar o break)
'''

string = 'Valor Qualquer'
i=0
while i < len(string):
    letra = string[i]

    print(letra)
    i+=1
else:
    print('Entrou no Else')



string = 'Valor Qualquer'

i=0

while i < len(string):
    letra = string[i]
    
    if letra == ' ':
        break

    print(letra)
    i+=1
    
else:
    print('Entrou no Else')