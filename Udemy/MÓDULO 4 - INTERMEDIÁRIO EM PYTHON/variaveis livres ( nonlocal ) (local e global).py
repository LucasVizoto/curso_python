# NONLOCAL
# locals() = mostra as variáveis locais da função
# globals() = mostra as globais
def fora(x):
    a=x

    def dentro():
        print(locals())
        print(dentro.__code__.co_freevars) #Mostra as varáveis livres da função
        return a 
    # a função dentro não está definida na função de dentro, mas na fora
    return dentro
# a é uma variável livre pois não está dentro do escopo da função dentro

dentro1 = fora(10)

#----------------------------------------------------------------
def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar):
        nonlocal valor_final # chave principal para isso  
# se não houvesse esse nonlocal, o python NÃO encontraria a variavel valor_final
# pois, por mais que seja uma variável livre, ela não está definida no escopo dele
# conceito de variáveis livres se resume em, retornar o valor de funçoes acima, mas 
# não usalas
        valor_final+=valor_a_concatenar
        return valor_final
    return interna

c = concatenar('a') #seta a variável c como a função com o valor 'a' pré definida

print(c('b'))
print(c('d'))
print(c('e'))
