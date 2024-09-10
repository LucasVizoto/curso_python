# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.
import json
import string
import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')

def converte_para_brl(numero: float| int )-> str:
    brl = 'R$' + locale.currency(val=numero, symbol=False, grouping=True)
    return brl 

data = datetime(2022,5,18)
dados = dict(
    nome = 'Lucas',
    valor = converte_para_brl(1_234_456),
    data = data.strftime('%d/%m/%Y'),
    empresa= 'Bro Technologies',
    telefone= '(11) 99999-9999'
)

# print(json.dumps(dados, indent=2,ensure_ascii=False))

# texto = '''
# Prezado(a) $nome,

# Informamos que sua mensalidade será cobrada no valor de $valor no dia $data. Caso deseje cancelar o serviço, entre em contato com a $empresa pelo telefone $telefone

# Atenciosamente,

# ${empresa},
# Abraços
# '''
# template = string.Template(texto)
# print(template.substitute(dados))


from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula1.txt'

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    texto = arquivo.read()
    template = arquivotemplate = string.Template(texto)
    print(template.substitute(dados))

# class MyTemplate(template):
#     delimiter = '%'
# muda o delimitador que é usado para amostrar as variáveis