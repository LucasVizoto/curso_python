''' 
and - Todas as condições precisam ser Verdadeiras (True) Tabela Verdade
São considerados Falsy (Valores considerados Falsos quando confrontados com o Booleano) 0 0.0 False
None é o inexistente, logo também é Falso
'''
entrada = input('[E]ntrada ou [S]air')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
# if executa quando ambas são verdadeiras. o códiogo só funciona se a senha for igual a permitida
if entrada == 'E' and entrada == senha_permitida:
    print('Entrando')
else :
    print('Saindo')    

'''
Or - Qualquel valor Verdadeiras (True) Valida a explessão toda como Verdadeira 
'''   
entrada = input('[E]ntrada ou [S]air')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
# if executa quando ambas são verdadeiras. o códiogo só funciona se a senha for igual a permitida
if entrada == 'E' or entrada == 'e':
    if entrada == senha_permitida:
        print('Entrando')
    else:
        print('Senha Inválida')    
else :
    print('Saindo')  

# Casos lógicos de se usar o Or
senha = input('Senha ') or 'Sem senha' #Se dar enter sem nenhum valor digitado ele retorna o segundo

senhaValida = '12345' or '54321' or 'arroz' or 'paodeforma'

if senha == senhaValida:
    print('Senha valida')

#-----------------------------------------------------------
#not inverte o booleano

senha = input('Senha: ')
if senha != senhaValida or not senha: #Se não for digitado ou se for diferente
    print('Senha incorreta')