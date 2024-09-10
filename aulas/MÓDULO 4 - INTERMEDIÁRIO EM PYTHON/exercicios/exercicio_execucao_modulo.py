# adiar a execução da função

def soma (x,y):

    return x+y

def multiplicacao (x,y):
    return x*y

def executa_funcao(funcao, x):
    def interna(y):
        return funcao(x,y)
    return interna
# vai receber a função, executar, e retornar o que foi executado após essa execução
# escopo interno / closure fechar o código depois

soma_com_cinco = executa_funcao(soma, 5)
multiplicacao_com_dez = executa_funcao(multiplicacao, 10)

print(soma_com_cinco(10))
print(multiplicacao_com_dez(12))

# sinceramente achei que era um bagulho mais complexo, mas é basicamente aquele reaproveitamento de
# parametros que já foi visto, cria-se uma função com um argumento pré setado, e quando algume for inserir
# alguma coisa, isso cai no parâmetro da segunda função, opis o primeiro jaá estava nesse pré set