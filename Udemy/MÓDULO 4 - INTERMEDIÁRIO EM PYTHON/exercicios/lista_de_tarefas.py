#rubber duck debbuging
import os
import json
# tarefas = []
# removidos = []
# while True:
#     print('Comandos: Listar, Desfazer, Remover x, Refazer')
#     receptor = input('Digite uma tarefa ou comando: ')
#     if receptor == 'break':
#         os.system('cls')   
#         break
#     elif receptor.lower() == 'listar':
#         print(f'TAREFAS: \n')
#         for item in tarefas:
#             print(item)
#         print('\n')    
#     elif receptor.lower() == 'desfazer':
#         if not tarefas:
#             print('Nada a Desfazer')
#         else:
#             removidos_variavel = tarefas.pop()
#             removidos.append(removidos_variavel)
#             os.system('cls')   
#     elif receptor.lower() == 'Desfazer x':
#         if not tarefas:
#             print('Nada a Remover')
#         else:
#             indice = int(input('Digite a posição do que deseja remover'))
#             tarefas.pop(indice-1)
#     elif receptor.lower() == 'refazer':        
#         if not tarefas:
#             print('Nada a Remover')
#         else:
#             tarefas_variavel = removidos.pop()
#             tarefas.append(tarefas_variavel)
#     else:
#         tarefas.append(receptor)
#         os.system('cls')

# print(f'Sua lista de tarefas ficou assim: \n')        
# for item in tarefas:
#     print(item)

#modularizar esse exercicio é uma boa, mas agora tô com preguiça
# sempre que puder, for preciso e possível, evitar o uso de condicionais, por conta da complexidade do código
# guared clouse é interessanet para se estudar depois

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados


CAMINHO_ARQUIVO = 'aula119.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)