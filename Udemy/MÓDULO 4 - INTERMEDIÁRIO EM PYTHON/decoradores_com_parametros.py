def fabrica_de_decoradores(a=None, b=None, c = None): 
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        def aninhada (*args, **kwargs): #nested funcction, uma função dentro de outra (lembrando que os valores são empacotados em cima para depois serem desempacotados abaixo)
            print('Decoradora 2')
            resultado = func(*args, **kwargs)
        
            return resultado
        
        return aninhada
    return fabrica_de_funcoes
# fazendo isso você tem acesso a três escopos de função, pois estão todas uma dentro da outra


@fabrica_de_decoradores(1,2,3)
def soma(a,b):
    return a+b
# vai gerar novos decoradores com base na execução dos paâmetros passados


multiplica =  fabrica_de_decoradores()(lambda x,y : x*y)

variavel = soma(10,5)
print(variavel)

