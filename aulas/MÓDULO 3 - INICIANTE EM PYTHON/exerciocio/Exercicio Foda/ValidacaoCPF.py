"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

1º PASSO - Somar todos os resultados: 
70+36+48+5612+20+32+27+0 = 301

2º PASSO - Multiplicar o resultado anterior por 10
301 * 10 = 3010

3º PASSO - Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7

4º PASSO - Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

Para calcular o segundo digito, é a mesma coisa, a unica diferença é que
no 1° PASSO é acrescida o valor do novo dígito gerado

"""
import re #regular expression
import sys 
cpf = '412.707.438-80'.replace('.', '').replace(' ', '').replace('-', '')
#.replace() pega o valor digitado no primeiro parâmetro e substitui pelo segundo valor

entrada = input('Digite seu CPF: ')
cpf = re.sub(
    r'[^0-9]', #subtitui itens de 0 a 9 que não são numeros (^)
    '', #substitui para esses valores
    entrada #pega desse lugar        
             )

entra_sequencial =  entrada == entrada[0]* len(entrada) 

if entra_sequencial: # isso é para evitar a validação de 111.111.111-11
    print('Você enviou dados sequenciais.')
    sys.exit() # esse comando ffaz encerrar o python (quando chega aqui ele para)

nove_digitos = cpf[:9] #Fatiamento para pegar os valores
contador_regressivo = 10

soma_multiplicacao = 0 
for digito in nove_digitos:
    soma_multiplicacao += int(digito) * contador_regressivo # lança o forEach digito
    #(1º PASSO)
    contador_regressivo -= 1 #Faz a conta do 10 até 2
primeiro_digito = 0 if (soma_multiplicacao*10)%11 > 9 else (soma_multiplicacao*10)%11 #2º, 3º e 4º PASSO
print(primeiro_digito)
'''
O primeiro digito recebe 0 se a soma das multiplicações E o módulo por 11 for maior do que nove]
senao recebe o próprio valor

if (soma_multiplicacao*10)%11 > 9:
    primeiro_digito = 0
else:
    primeiro_digito = (soma_multiplicacao*10)%11

'''
dez_digitos = nove_digitos + str(primeiro_digito)

contador_segundo_digito = 11
soma_multiplicacao_segundo = 0

for digito in dez_digitos:
    soma_multiplicacao_segundo += int(digito)*contador_segundo_digito
    contador_segundo_digito -= 1

segundo_digito = 0 if (soma_multiplicacao_segundo*10)%11 > 9 else (soma_multiplicacao_segundo*10)%11  #Ternário que diz se a condição for satisfeita  = 0
print(segundo_digito)

cpf_valido = dez_digitos+str(segundo_digito)
if cpf_valido == cpf :
    print('CPF válido')
else:
    print('CPF inválido')    