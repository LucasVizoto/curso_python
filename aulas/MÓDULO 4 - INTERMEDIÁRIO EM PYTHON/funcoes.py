'''
introdção às funçoes (def) em Python

funções são trechos de código usados do seu codigo
elas recebem parâmetros e retorna um valor específico
Por padrao, funcoes em Python retornam None
 '''

def python ():
    ...

def saudacao(nome = 'Sem Nome'): #esse igual é o valor a ser inserido quando não são colocados parâmetros 
    print(f'Olá {nome}')

saudacao('lucas')
saudacao('Bia')
saudacao()

'''
Argumentos nomeados e não nomeados em funções Python
Argumentos nomeados tem nome com sinal de igual
Argumentos não nomeados recebe apenas o argmento (valor)

soma(1,2)
soma(x=1, y=2) (Argumento nomeado)
basicamente usar o parâmetro no argumento
'''
def soma(x,y):
    print(x+y)

print(soma) #mostra o id na memória da função
soma(x=1, y=2)
soma( 1, 2)


#-------------------------------------------------------------------------

'''
Valores padrão para parãmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja enviado
para o parametro, o valor padrão será usado

Melhorar = Refatorar == editar o código
'''
def soma(x, y, z=None): #No caso de atualizações isso é importante para ver se foi passado ou não o novo paâmetro
#Toda vez que colocar um valor com um valor padrão, os próximos necessariamente precisarão receber também uma nomeação
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)


soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(y=9, z=0, x=7)

