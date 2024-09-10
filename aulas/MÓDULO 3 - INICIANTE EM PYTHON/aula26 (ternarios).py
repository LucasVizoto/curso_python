'''
valor) if (condição) else (outro valor)
if ternario
'''
print('valor' if True else 'Outro valor')  
print('valor' if False else 'Outro valor')  
#----------------------------------------------------------------
Condicao = True
variavel = 'Valor' if Condicao is True else 'Outro valor'
# Se a condição é verdadeira , 'Valor', se não 'Outro valor

#----------------------------------------------------------------
digito = 9
novo_digito = digito if digito <= 9 else 0
#novo_digito recebe digito SE digito for menor igual 9 SENAO novo digito recebe 0 
''' 
É a mesma coisa que:
 if digito <= 9:
    novo_digito = digito
 else:
    novo_digito = 0



print('valor' if True else 'Outro Valor' if True else 'Qualquer coisa')
isso em cima é basicamente um elif em ternário, pois o else possui um if dentro dele
if True:
    print('Valor')
elif True:
    print('Outro valor')
else:
    print('Qualquer coisa')        

'''