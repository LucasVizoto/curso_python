"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
def exercicio_1():
    n1 = int(input('Digite um número inteiro: '))
    try: #Tratamento de erro pra caso o usuario digite uma String
        if n1 % 2 == 0: # Verifica se é Par
            print(f'O número {n1} é par')
        else:
            print(f'O número {n1} é ímpar')
    except: #Se crashar ele cai aqui
        print('Não é um número inteiro')

def exercicio_2():
    try:
        hora_atual = int(input('Digite a hora atual'))
        bom_dia = hora_atual >= 0 and hora_atual<=11
        boa_tarde = hora_atual>= 12 and hora_atual<=17
        boa_noite = hora_atual >= 18 and hora_atual<=23
        if bom_dia:
            print('Bom dia')
        if boa_tarde:
            print('Boa tarde')
        if boa_noite:
            print('Boa noite')
    except: 
        print('Hora inválida')

def exercicio_3():
    primeiro_nome = input('Digite seu Primeiro nome: ')
    tamanho_nome = len(primeiro_nome)
    try:
        
        if tamanho_nome <= 4:
            print('Seu nome é curto')
        elif tamanho_nome== 5 or tamanho_nome==6:
            print('Seu nome é normal')
        elif tamanho_nome>6:
            print('Seu nome é muito grande')       
    except:
        print(' INVÁLIDO ')          
