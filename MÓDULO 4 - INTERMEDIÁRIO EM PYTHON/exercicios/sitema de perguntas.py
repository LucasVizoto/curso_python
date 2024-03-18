# Exercício - sistema de perguntas e respostas


perguntas = [
# Todas as perguntas inseridas aqui devem conter as chaves
# Pergunta, Opções, Resposta

    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
] #Vetor de Objetos
certas = 0 # iniciando a contagem de respostas corretas

for i in range(len(perguntas)): # Para i no length de perguntas (Para caso sejam adicionadas mais)
    print(perguntas[i].get('Pergunta'), '\n') #perguntas. get para retornar o valor e a String nos parâmetros de get é o valor a ser impresso

    for item, valor in enumerate(perguntas[i].get('Opções')): 
    #enumerate retorna indice e valor, logo podemos usálo para seguir esta lógica, pois se adicionadas mais opções não irá dar um erro
        print(f'{item}) {valor}')
    try:      
        resposta = int(input('Escolha uma opção: '))
    except ValueError:
        print('Infelizmente você errou... ❌ \n')
        continue
    try: # try / except para fazer o tratamento de erro para caso o usário digite um indice que não existe
        if perguntas[i].get('Resposta') == perguntas[i].get('Opções')[resposta]:
        # a lista perguntas, no indice atual (obj que estamos neste momento do for) pega a resposta correta e compara pra ver se é igual a
        # lista perguntas, no indice atual pegando a lista de opções no indice de resposta (opção escolhida pelo usuário)  
            print('Parabens você acertou ✅🎉 \n')
            certas += 1
        else:
            print('Infelizmente você errou... ❌ \n') 
    except IndexError: #erro gerado caso o indice estoure
        print('Infelizmente você errou... ❌ \n') #conta como errado e não contabiliza a contagem


# print do resultado do questionário abaixo, com variações para a quantidade de acertos
if certas == 0:
    print('Sinto muito, mas você infelizmente errou todas 😓')
elif certas < len(perguntas)/2 :
    print(f'Você acertou {certas} \
          \nDe {len(perguntas)} perguntas \
          \nO que representa que você acertou menos da metade das questões 😰 ')   
else:
        print(f'Você acertou {certas} \
          \nDe {len(perguntas)} perguntas 😶‍🌫️')    