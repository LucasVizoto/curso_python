dict_alunos = {'Bob': 68,
               'Michel': 84,
               'Zico': 57,
               'Ana': 93}

dict_alunos_status = {k:v for k, v in dict_alunos.items()} 
print(dict_alunos_status)
## Criando uma comprehension num dicionário

dict_alunos_status = {k:('Aprovado' if v > 70 else 'Reprovado') for (k,v) in dict_alunos.items()}
print(dict_alunos_status)
# Fazendo uma dict comprehension com um condicional