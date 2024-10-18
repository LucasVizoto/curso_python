'''
crie um exercicio que duplique, triplique e quadruplica o nº recebido pelo ususário
'''

numero = int(input('Insira um número: '))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero*multiplicador
    return multiplicar 

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(numero))
print(triplicar(numero))
print(quadruplicar(numero))