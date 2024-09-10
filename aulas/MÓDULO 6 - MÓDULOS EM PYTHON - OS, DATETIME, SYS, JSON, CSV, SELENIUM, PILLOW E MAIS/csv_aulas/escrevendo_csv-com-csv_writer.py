import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula2.csv'

lista_clientes = [
    {'Nome': 'Lucas Vizoto','Endereco': 'Av 1, 22'},
    {'Nome': 'Beatriz Meleti', 'Endereco': 'Av 1, 22'},
    {'Nome': 'Gabriel Silva', 'Endereco': 'R. 2, "1"'},
    {'Nome': 'Ulisses Martins', 'Endereco': 'Av B, 3A'},
    #... adicionar mais clientes aqui
]

with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.writer(arquivo)

    escritor.writerow(nome_colunas)
   
    for cliente in lista_clientes:
        print(cliente.values())
        escritor.writerow(cliente.values())


# outra alternativa é por dicionário:

with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
        )
    
    escritor.writeheader() # escreve o cabeçalho e depois os dicionários
    
    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)

