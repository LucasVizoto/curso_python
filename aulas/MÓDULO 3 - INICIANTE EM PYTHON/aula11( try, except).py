'''
try -> Tentar executar o código 
except -> ocorreu algum problema ao tentar executar

é a mesma coisa que o Try Catch do JS
'''

print(1234)
print('sfwifmwes')
int('a') # Retrona um ValueEror (estoura ums exceção) (aparece um erro)
#--------------------------------------
numero_str = input('Digite um número')

print(numero_str.isdigit()) #Retorna True ou False caso o objeto analisado tenha apenas digitos inteiros

if numero_str.isdigit():
    numer_float = float(numero_str) #se não tratar ia repetir o numero por 2 vezes  
    print(f'O dobro de {numero_str} é {numer_float * 2 :.2f}')
else:
    print('Não é um número')
#-------------------------------------- #o if checa a condição e muda o fluxo dependendo do valor (não evita erros (ou exceções em Python))

try: 
    numer_float = float(numero_str)
    print('Float', numer_float) 
    print(f'O dobro de {numero_str} é {numer_float * 2 :.2f}')
except:
    print('Não é um número') 

#Se acontecer um erro dentro do TRY pela pro EXCEPT  

# Esse tratamento de erro é usado para caso o usuario tenha digitado, sla, 'a'
# Nesse caso não seria possivel a converção e por isso o try except é uma boa
#O if crasharia e nn executaria o else