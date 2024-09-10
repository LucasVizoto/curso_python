#empacotamento e desempacotamento de dicionários
a,b = 1,2
a,b = b,a
print(a,b)
#empacotamento

pessoa = {
    'nome' : 'Beatriz',
    'sobrenome' : 'Meleti'
}
a,b = pessoa.values()
(a1, a2), (b1,b2) = pessoa.items()
print(a1,a2)
print(b1,b2)

#args e kwargs
# kwargs - keyword arguments (argumentos nomeados) 

dados_pessoa = {
    'idade': 17,
    'altura' : 1.7
}


pessoa_completa = {**pessoa, **dados_pessoa}
#empacotamento do dicionário

def mpstra_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS', args)
    print('NOMEADOS', kwargs) #VEM SEPARADO COM NOME DESSA CHAVE E VALOR

mpstra_argumentos_nomeados(1, 2, nome = 'lucas', random = 123)    

#pode tambem desempacotar para passar o valor
mpstra_argumentos_nomeados(**pessoa_completa)