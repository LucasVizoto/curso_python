from salvando_em_json import CAMINHO_DO_ARQUIVO, Pessoa, fazer_dump
import json
with open(CAMINHO_DO_ARQUIVO, 'r') as arquivo:
    dados = json.load(arquivo)
    p1 = Pessoa(**dados[0])
    p2 = Pessoa(**dados[1])
    p3 = Pessoa(**dados[2])
