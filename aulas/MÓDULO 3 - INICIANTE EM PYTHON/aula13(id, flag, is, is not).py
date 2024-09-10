'''
Flag (Bandeira) - Marcar um local
None = Não Valor
is e is not = é ou não é (tipo vaor identidade) (Checa a identidade pra ver se é alguma coisa)
id = Identidade
'''

v1 = 'a'
print(id(v1)) # Valor da variável na memória (por isso do numeor grande)

#importante para uso de objetos
#Como o python busca tal elemento

#----------------------------------------------------------------

condicao = False
passou_no_if = None #Não tem valores setados na variávle, logo, False
if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça nada')    
print(passou_no_if, passou_no_if is None) #passou_no_if == None (mesma coisa)   
print(passou_no_if, passou_no_if is not None) # Como o not inverte, "Se NÃO é none" 
# is retorna True ou False, pois é uma pergunta (passou no if é None ?)

'''
Exemplos: 

if passou_no_if is None:
    print('Não passou no if')
if passou_no_if is not None: 
    print('Passou no if')

'''
