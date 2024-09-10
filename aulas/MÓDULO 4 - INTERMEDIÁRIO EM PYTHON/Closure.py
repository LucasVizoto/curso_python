'''
funções que retronam outras funções
closure nada mais é do que o salvamento das informações na memória
e é retornado quado chamado novamente
'''
def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar

saudacao_1 = criar_saudacao('Bom dia', 'Lucas')
saudacao_2 = criar_saudacao('Bom dia', 'Bia')

print(saudacao_1())
print(saudacao_2())

#-----------------------------------------------------

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')


print(falar_bom_dia('Lucas')) #Recebe a função com um parâmetro já pré setado, pois este está na variável
print(falar_bom_dia('Bia'))