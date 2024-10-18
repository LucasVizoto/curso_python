# print("OI")
# python .\aula_dir_E_help\main.py para executar no terminal

import documentando_funcoes as df
import uma_linha
import varias_linhas
import documentando_classe as dc

dir(uma_linha) # método que mostra tudo que tem dentro de uma linha
print(dir(uma_linha))
#dir retirna uma lista de string com tudo que tem no módulo
print(uma_linha.__doc__) # retorna docstrings
print(uma_linha.__file__) # retorna o caminho do arquivo
print(uma_linha.__name__) # nome do modulo

help(uma_linha) 
#retorna tudo junto, NAME(com doc), FILE, FUNCTIONS e DATA(variaveis com seu retorno) 
# sair é so apertar um "q"
# docstring são coisas com três aspas
help(varias_linhas)
help(df) # documentando funcoes
help(dc)

# Você pode documentar funções, classes coisas simples ou até complexas 




