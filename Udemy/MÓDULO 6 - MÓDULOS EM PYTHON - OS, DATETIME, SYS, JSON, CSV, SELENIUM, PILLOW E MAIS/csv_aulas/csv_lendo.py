# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / "aula1.csv"
# print(CAMINHO_CSV)

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for line in leitor:
        print(line)
        # print(line[0], line[1])
        # voceê vai iterando e mostrando o valor que deseja da linha

# OU TAMBEM PODE SER FEITO DA SEGUINTE FORMA

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha['Nome'], linha['Idade'], linha['Endereco'])
# neste caso iteramos com em um dicionário 