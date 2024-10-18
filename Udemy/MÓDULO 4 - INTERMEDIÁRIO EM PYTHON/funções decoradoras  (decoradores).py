# funções decoradoras e decoradores
# decorator = recebendo alguma coisa, decora e retornando outra coisa
# decorar = Adicionar/ Remover /Restringir / Alterar (CRUD ???)
# funções decoradoras são funções que decoram outras funções
# decoradores são usados para fazer o Python usar as funções decoradoras em 
# outras funções 
def criar_funcao(func):
    def interna(*args, **kwargs):
        # decora a função aqui
        for arg in args:
            is_string(arg)   
        resultado = func(*args, **kwargs)
        # função decorada
        return resultado
    return interna
# função decoradora, pois recebe a função para depois fazer uma Closure
# a função interna será retornada pois a decorada é outra


def inverte_string(string):
    return string[::-1]
def is_string(param):
    if not isinstance(param, str):
        raise TypeError('O parametro deve ser uma string')
# função para checar se é ou não uma String    

inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('Lucas')

print(invertida)

# no final são declarados variáveis que vão chamar as funções para verificar e para 
# inverter a String

# na parte de criar_funcao, ela possui uma função interna recebendo os argumentos
# nesta função interna ele chama a função para verificação de Strings, verificando cada 
# argumento passado no empacotamento args

# a função de verificação possui um raise TypeError para levantar e parar o programa caso um
# argumento passado no empacotamento args, não seja uma String. ao final, caso todos os argumentos passem, 
#                     ela chama a função interna para inverter a String

#----------------------------------------------------------------

# decoradoras 'Syntax_sugar' Açucar sintático
# traduzindo, açucares sintáticos são funções que irão poupar nosso trabalho 
# e, ao invés de fazer oq foi feito na outra aula, a função faz isso por vocÊ

# decorador
@criar_funcao #Açucar sintático
def inverte_string_nova(string):
    print(inverte_string_nova.__name__) # com o rolê do sugar, a função muda de nome para interna, ois vai passar por lá primeiro
    return string[::-1]
print (inverte_string_nova('JDNFSDFNAAFASJDASDBL'))

# variavel_nova vai chamar a inverte_string_nova recebe a criar_função antes 
# da execução

#----------------------------------------------------------------


