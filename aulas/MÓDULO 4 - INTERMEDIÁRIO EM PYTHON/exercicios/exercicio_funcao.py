# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicacao(*resto):
    total = 1
    for numero in resto:
        total *= numero
        return total
    
def par_impar(x):
    if x%2==0:
        return print('PAR')
    return print('IMPAR')

resultado = multiplicacao(1,2,3,4,5,6,7,8,9,10,11,12)
icognita = int(input('Insira um valor e veja se ele é par ou impar: '))
