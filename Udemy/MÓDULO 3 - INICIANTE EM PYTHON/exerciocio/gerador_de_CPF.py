
import random

nove_digitos =''
for i in range(9):
    nove_digitos += str(random.randint(0,9))
contador_regressivo = 10

soma_multiplicacao = 0 
for digito in nove_digitos:
    soma_multiplicacao += int(digito) * contador_regressivo # lança o forEach digito
    #(1º PASSO)
    contador_regressivo -= 1 #Faz a conta do 10 até 2
primeiro_digito = 0 if (soma_multiplicacao*10)%11 > 9 else (soma_multiplicacao*10)%11 #2º, 3º e 4º PASSO
print(primeiro_digito)

#------------------------------------------------------------------------------

dez_digitos = nove_digitos + str(primeiro_digito)

contador_segundo_digito = 11
soma_multiplicacao_segundo = 0

for digito in dez_digitos:
    soma_multiplicacao_segundo += int(digito)*contador_segundo_digito
    contador_segundo_digito -= 1

segundo_digito = 0 if (soma_multiplicacao_segundo*10)%11 > 9 else (soma_multiplicacao_segundo*10)%11  #Ternário que diz se a condição for satisfeita  = 0
print(segundo_digito)

print(f'{nove_digitos}{primeiro_digito}{segundo_digito}')