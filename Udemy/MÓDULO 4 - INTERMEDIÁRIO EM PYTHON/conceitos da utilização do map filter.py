#mapeamento de dados usando map na list comprehension
# mapeamento é pegar os dados jogar numa lista de mesmo tamanho
produtos = [
    {'nome' : 'Notebook', 'preco' : 1000},
    {'nome' : 'Mouse', 'preco' : 2000},
    {'nome' : 'Teclado', 'preco' : 3000},
    {'nome' : 'Monitor', 'preco' : 4000}
]
novos_produtos = [produto for produto in produtos]

print (*novos_produtos, sep='\n')
#separador usado para exibir cada item é a quebra de linha

nome_produtos = [produto['nome'] for produto  in produtos]
print(*nome_produtos, sep='\n')



#dá também para coocar dicionários nas listas
aumento_de_preco_nos_produtos = [{**produto, 'preco' : produto['preco']*1.05} for produto in produtos]
print(aumento_de_preco_nos_produtos, sep = '\n')
#empacotou o dicionário nesta lista e depois aplicou o aumento em 5% de cada preço já listado

# DA TAMBÉM PRA COLOCAR IF TERNÁRIO. COLOCA-SE A ESQUERDA DO FOR, ENTÃO É BASICAMENTE A CRIAÇÃO DE UMA CONDIÇÃO E
# SE AQUILO ACONTECER, É EXECUTADO O FOR 

if_ternario = [
    {**produto, 'preco' : produto['preco']*1.05} # o que vai ser colocado na lista
    if produto['preco'] > 20 else {**produto} #se for maior que 20 executa, se não, continua o mesmo
    for produto in produtos #condição do for
] 

#----------------------------------------------------------------
# LIST OCMPREHENSION COM MAIS DE UM FOR

lista_douze = [(x,y) for x in range(3) for y in range(3)]
# BASICAMENTE TUPLAS MATRIZ
print (lista_douze)
    #É BASICAMENTE ISSO
    #lista = []
    #for x in range(3):
    #    for y in range(3):
    #        lista.append((x,y))
#----------------------------------------------------------------

# FILTER 


lista_nova_denovo = [n for n in range(10) if n < 5]
#filtro do que vai entra 

# inclui o numero enquanto satisfaz a condição
print(lista_nova_denovo)

# NOTAS DO BURRO : filtar é basicamente colocar o if depois do for
# mapear é usar esse for ternário para gerar uma nova lista com base em outras coisas 