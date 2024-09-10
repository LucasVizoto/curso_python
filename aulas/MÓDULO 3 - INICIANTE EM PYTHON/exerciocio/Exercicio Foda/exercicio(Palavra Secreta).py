"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os 

# importando a biblioteca os (biblioteca de comandos do Sistema Operacional) (IOS, Linux, Windows)
# usada para dar o clear no Terminal (cls no cmd)
# https://www.hashtagtreinamentos.com/biblioteca-os-no-python (link explicando)

senha_secreta = 'amor'
tentativas = 0
situacao_usuario = '*'*len(senha_secreta) # o caractere * repete a quantidade de vezes igual ao length da String
#setar as variáveis para logo abaixo iniciar o do while 

while True: #Do
    
    letra = input(f'Digite apenas uma letra para adivinhar: ').lower() #Letra a ser digitada pelo usuário formatada como minúscula para entrar caso o usuario coloque em maiusculo
    
    if letra in senha_secreta: # Se letra existe em senha_secreta
    
        for contador_posicao in range(len(senha_secreta)):  #for para verificar letra por letra, por isso o range é o length da senha 
    
            if letra == senha_secreta[contador_posicao]: # se a letra for identica a letra referente ao indice da senha secreta .
                situacao_usuario = situacao_usuario[:contador_posicao] + letra + situacao_usuario[contador_posicao + 1:] 
                # situacao_usuario que antes só tinha * , agora recebe a nova letra no lugar certo. FATIAMENTO. 
                # recebe a situação até o contador, insere a letra, depois insere o resto (resto pq é do contador +1 : até o final )
                # x = x[0:contador] (de 0 até o contador) + letra + x[contador+1 : 0]
    
    tentativas += 1
    
    if len(letra)>1: #Tratamento de erro para o caso de ser digitado mais de uma letra
        print(f'Foi contada uma tentativa e você digitou mais de uma letra... Digite APENAS uma letra ')   
        
    print(f'Situacao Atual: {situacao_usuario}')
    
    if situacao_usuario == senha_secreta:
        os.system('cls')
        break #QUEBRA O WHILE    / DO { ... }WHILE( condição)


print(f'VOCÊ GANHOU PARABÉNS !!!\
      \nA palavra era: {senha_secreta}\
      \nVocê fez em {tentativas-len(senha_secreta)+1} Tentativa(s)') #Não conta as vezes que acertou. O +1 é pra não zerar e indicar que foi feito ao menos uma tentativa    

    