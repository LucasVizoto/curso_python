'''
Jogo da Adivinhação:
Crie um jogo em que o computador escolhe um número aleatório e o 
usuário tenta adivinhar qual é. O programa deve fornecer dicas
para indicar se o número é maior ou menor do que o palpite do usuário.

'''

import random #Import random para gerar um número aleatório
import os #import os para usar o Sistema Operacional e limpar o terminal no final
import time #import time para trazer uma biblioteca que mexe com tempo da vida real em seg
     


def tentativas_infinitas():
    numero_pc = random.randint(0,100) #Vai sortear um número inteiro aleatório entre 0 e 100
    tentativas = 0
    while True:
            numero_digitado = int(input('Digite seu palpite: '))
            if numero_digitado > numero_pc:
                print('O valor sorteado é MENOR que o digitado. ')

            if numero_digitado < numero_pc:
                print('O valor sorteado é MAIOR que o digitado')    
                
            tentativas+=1
            if numero_digitado != numero_pc: # Se diferente para não oferecer dicas caso o usuário acerte
                dica = input('\nDeseja receber alguma dica? (S)im ou (N)ão    ') 
                if dica.lower().startswith('s'):#Coloca em minúsculo e depois verifica se começa com S
                    if numero_pc%2==0: #divisivel por 2
                        print('O número é par')
                    else:
                        print('O número é ímpar')
                    print(f'Se elevado ao quadrado, seu valor é {numero_pc**2}')          

                elif dica.lower().startswith('n'): #Coloca em minúsculo e depois verifica se começa com N
                    print('OK, irei aparecer de novo caso arrependa')
                else:
                    print('Valor inválido')            
            

            if numero_digitado == numero_pc:
                os.system('cls') #Digita cls no Terminal
                print('Parabéns, você acertou!')
                print(f'Você resolveu em {tentativas} tentativas \n')   
                time.sleep(3)
                break
#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#Segunda forma que pensei em fazer o exercício
numero_sorteado = random.randint(0,100)
CONTADOR = 5
def contagem_regressiva():
    for i in range(CONTADOR):
        print(f'Você possui {CONTADOR-i} chances para acertar esse número')
        numero_digitado = int(input('Digite um número e tente acertar o escolhido pela máquina: '))
        if numero_digitado > numero_sorteado:
            print('O valor sorteado é MENOR que o digitado. ')

        if numero_digitado < numero_sorteado:
            print('O valor sorteado é MAIOR que o digitado')    
            
        if numero_digitado != numero_sorteado: # Se diferente para não oferecer dicas caso o usuário acerte
            dica = input('\nDeseja receber alguma dica? (S)im ou (N)ão    ').lower() 
            if dica.startswith('s'):#Coloca em minúsculo e depois verifica se começa com S
                if numero_sorteado%2==0: #divisivel por 2
                    print('O número é par')
                else:
                    print('O número é ímpar')
                print(f'Se elevado ao quadrado, seu valor é {numero_sorteado**2} \n')          

            elif dica.startswith('n'): #Coloca em minúsculo e depois verifica se começa com N
                print('OK, irei aparecer de novo caso arrependa \n')
            else:
                print('Valor inválido')
        
        if numero_digitado == numero_sorteado:
            os.system('cls') #Digita cls no Terminal
            print('Parabéns, você acertou!')  
            print(f'Você resolveu em {i+1} tentativas \n')
            time.sleep(3)
            break
    else: #se o for ser xecutado por completo, o else ativa
        os.system('cls') 
        print('Sinto muito... Quem sabe numa próxima   \n:) \n')    
        time.sleep(3)
        
#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------

while True:
    escolha = input('Escolha o que deseja fazer: \
                   \nA. Tentativas infinitas \
                   \nB. Tentativas limitadas \
                   \nC. Sair \n ')
    if escolha.lower().startswith('a'):
        os.system('cls')
        tentativas_infinitas() #Chama a funcao def definida acima 

    elif escolha.lower().startswith('b'):
        os.system('cls')
        contagem_regressiva() # chama a funcão def definida aima

    elif escolha.lower().startswith('c') or escolha.lower().startswith('s'):
        os.system('cls')
        break  
    else:
        print('Valor inválido')