nome = 'Lucas Vizoto'
altura = 1.73
peso = 66
imc = peso / altura ** 2

#f-strings (formatation)
print(f'{nome} tem {altura :.2f} de altura')
print(f'pesa {peso} quilos e seu imc é {imc:.2f}',) 

# Lucas Vizoto tem 1.73 de altura,
# pesa 66 quilos e seu IMC é

numero1 = int(input('\n\nDigite um n '))
numero2 = int(input('Digite outro n ')) #
print(f'A soma dos números é {numero1+numero2}')