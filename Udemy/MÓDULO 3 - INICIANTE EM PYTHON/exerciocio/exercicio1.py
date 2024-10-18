"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome} !!
        Seu nome invertido é {nome invertido}!!!
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras !!!
        A primeira letra do seu nome é {letra} 1!!!!
        A última letra do seu nome é {letra}!!!

Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input('Digite seu Nome: ')
idade = int(input('Digite sua idade: '))

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome tem {len(nome)} letras')
    if ' ' in nome: 
        espacos = nome.count(' ') # count função que retorna o número de ocorrencias nos parâmetros
    print(f'Seu nome contem {espacos} espaços')
    print(f'A Primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')    
