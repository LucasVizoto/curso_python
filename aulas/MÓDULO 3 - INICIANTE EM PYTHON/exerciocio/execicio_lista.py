"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.

"""
import os
import time

lista_compra = []

while True:
    escolha = input('Selecione uma Opção: \n[i]nserir  [a]pagar  [l]istar  [s]air : ').lower()
    os.system('cls')
    if escolha.startswith('i'): 
        inserir = input('Qual item deseja adicionar a lista: ')
        lista_compra.append(inserir)
        os.system('cls')
    
    if escolha.startswith('a'):
        try:
            delete = int(input('Digite o índice do valor que deseja apagar: '))
            del lista_compra[delete]
            os.system('cls')
        except TypeError or IndexError:
            print('Não foi possível apagar este índice, digite L para analisar a lista')
            time.sleep(3)
            os.system('cls')
            continue
    
    if escolha.startswith('l'):
        for i, valor in enumerate(lista_compra):
           print(i,valor) 

    if escolha.startswith('s'):
        break    
