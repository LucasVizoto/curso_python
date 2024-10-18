# json.dumps e json.loads com strings + typing.TypedDict
# Dump = Jogar pra fora enquanto o Load = Puxar pra dentro
# Ao converter de Python para JSON

# Python        JSON
# # dict          object
# # list, tuple   array
# # str           string
# # int, float    number
# # True          true
# # False         false
# # None          null

import json
from pprint import print
from typing import TypedDict

class Movie(TypedDict): # para realizar a tipagem do dicionario
    title: str
    original_title: str
    is_movie : bool
    imdb_rating: float
    year: int
    characters: list
    budgets: None


doc_string = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''

# carregar a string pra dentro do python para ter esse objeto no python

movie: Movie = json.loads(doc_string)
print(movie, width=40) #realizou um print mais bonitinho pq importou de pprint

print(movie['title'])
print(movie['characters'])
print(movie['year'] + 10) # Como foi typado, ao colocar os colchetes o python sugere oq você pode colocar

# Jogado de python para json
string_json = json.dumps(movie, ensure_ascii=False, indent=2)
print(string_json) 
# ensure_ascii é para formatação dos acentos do texto json
# identar o json com 2 espaços

# -----------------------------------------------------------------------------------------------------------
# QUANDO SE TIRA O S NO NOME DO METODO É MANIPULAÇÃO DE ARQUIVO, ENQUANTO O DUMPS É DA STRING JSON


# realizando dump e load com arquivos
import json
import os

NOME_ARQUIVO =  'dump_e_load_com_arquivos.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath( #abspath retorna o caminho absoluto de algo
    os.path.join( # une duas coisas
        os.path.dirname(__file__), #nome do diretorios do arquivo + NOME_ARQUIVO
        NOME_ARQUIVO
    )
)
# UM JEITO MAIS FACIL SERIA COM PATHLIB
print(os.path.join(
    os.path.dirname(__file__),
    NOME_ARQUIVO)
    )


# print(json.load(doc_string))
# vai retonar convertido em  
filme = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',

    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}
print(filme)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    filme_do_json = json.load(arquivo)
    print(filme_do_json)
