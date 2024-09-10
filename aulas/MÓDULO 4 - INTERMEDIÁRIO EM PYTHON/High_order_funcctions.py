'''
funções de primeira classe
as funções em python podem ser tratadas como qualquer tipo de dado

Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

Não faria muita diferença no seu código, mas penso que deveria lhe informar isso.

Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.
'''
def saudacao(msg):
    return msg

def executa (funcao, msg): #uuma função sendo executada no parâmetro de outra função
    return funcao(msg)

saudacao_2 = saudacao('Bom Dia') #aponta a função
v = executa(saudacao_2)
print(v)
#as funções podem ser colocadas em variáveis, e parâmetros e adminitradas da forma que quiser