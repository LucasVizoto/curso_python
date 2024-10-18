'''
interpolaçãio de Strings é basicamente escrever em C
 s - String
 d, i - interger
 f - float
 x, X - Hexadecimal
'''

nome = 'Lucas'
preco = 1000.95315612
print('%s o preco do é R$%.2f' % (nome, preco)) #.2 coloca duas casas após a vírgula

hexa = int(input('Digite um número: '))
print('O hexadecimal de %i é %x' % (hexa, hexa))