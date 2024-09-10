def executa(funcao, *args):
    return funcao(*args)

def soma(x,y):
    return x+y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero*multiplicador
    return multiplica


print(executa(lambda x,y: x+y,
              2,3)) #jogou como valores do parametro para teste

duplica = cria_multiplicador(2)
duplica = executa(lambda m: lambda n: n*m)
#lambda é a arrow functon lambda => 
# function nome_modulo() {}
# m e n sao os item a serem passados de parâmetros, caso deseja inserir um valor, basta colocar virgula e o valor no final