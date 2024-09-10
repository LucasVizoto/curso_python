'''
condicionais if/ elif /else (elif é o else if(){}  )
'''
entrada = input('Entrar ou Sair ')
# or significa OU e and significa E
if entrada == 'Sair' or entrada == 'sair':
    print('Saindo')
elif entrada == 'entrar' or entrada == 'Entrar':
    print('Entrando') #NOTA**** TOMAR MUITO CUIDADE COM IDENTAÇÃO
else:
    print('Não digitou argumento válido')

'''----------------------------------------------------------------'''
condicao = True

if condicao:
    print('Condicao verdadeira')
else:
    print('Condicao falso')    
print('fora do if')   

'''----------------------------------------------------------------'''
#debug para na breakpoint (bolinha vermelha do lado do código)
'''----------------------------------------------------------------'''
primeiro_valor =  input('Digite um valor')
segundo_valor = input('Digite outro valor')

if primeiro_valor > segundo_valor:
    print(f'primeiro_valor ({primeiro_valor}) é maior que o segundo_valor ({segundo_valor})')
elif primeiro_valor < segundo_valor:
    print(f'segundo_valor({segundo_valor}) é maior que o primeiro_valor({primeiro_valor})')    