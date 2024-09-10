'''
Escopo de funções em Python
oq está na funcão fica na função
Escopo significa o local onde aquele código pode atingir 
Existe o escopo global e local
global - Todo código é alcançável
local - apenas nomes do mesmo local podem ser alcançados

A palavra global faz um avariável do escopo externo ser a mesma no escopo interno
'''
x = 2
# x num escopo global

def escopo(parametros):
    global x
    x=10 #está no escopo da função, se tentar acessar o x fora da função nn funciona
    #não é o mesmo x, pois este esá num escopo local
    #oq acontece aqui não altera o externo, exceto com global
    print(x)

escopo()   
print(x) 
'''
 Se você usar global numa variável de fora, você irá manipular ela 
 dentro da função, logo, x global deixa de ser 2 e passa a receber 10
 como definido na função 
 quando criado um novo módulo cria-se um espaço na memória destinado para
 salvar as variáveis e coisas que irão acontecer no módulo no
 CALL STACK (pilha de chamadas) (função dentro de função é um ótimo exemplo)

 
        USO DE RETURN
funções retonam por padrão None, a naõ ser que você use um return        
'''

variavel = print('Bia')
print(variavel)

def soma (x, y):
    return x+y #A sua função receberá esse valor, return também idica parada da função

soma1 = soma(2, 2)
soma2 = soma(3,3) 
print(soma1+soma2)

'''
args - Argumentos não nomeados
*args (empacotamento e desempacotamento)
 lembre-se de desempacotar
'''
x,y, *resto = 1,2,3,4,5,6


def soma(*args): #empacotou em tupla
    total = 0
    print(args, type(args)) #retorna uma Tupla
    for numero in args:
        print(total)
        total += numero
        return total

somatoria = soma(1,2,3,4,5,6,7,8,9,10)
print (somatoria)
#-------------------
'''
funçao sum soma os valores de dois números, mas se passar uma tupla dá certo
'''
numeros = 1,2,3,4,5,6,7,8,9,10
print(numeros, type(numeros))
print(*numeros) #O * em uma variável empacotada, desempacota ela

print(sum(numeros))