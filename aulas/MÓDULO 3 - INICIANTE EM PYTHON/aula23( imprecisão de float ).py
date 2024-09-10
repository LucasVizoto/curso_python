'''

'''
import decimal

numero1 = 0.1
numero2 = 0.7
numero3 = numero1+numero2
print(numero3)

print(f'{numero3:.2f}') #formatou a float para arredondar em duas casas

print(round(numero3, 1)) #Arredonda e conta zeros a direita do float
#          variavel, casas após a vigula
#---------------------------------------------------------------------------

numero1 = decimal.Decimal(0.1)
numero2 = decimal.Decimal(0.7) #Só é usado se for um float MUITO grande. Só usado se a absoluta precisão é MUITO necessário
numero3 = numero1+numero2
print(numero3)

