# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo

import calendar 
print(calendar.calendar(2022))
# retorna no seu terminal literalmente o calendario do ano passado como param

print(calendar.month(2022, 5))
# retorna o calendario de Maio de 2022

print(calendar.monthrange(2022, 5))
# o segundo valor da tupla é o último dia do mês, enquanto o primeiro valor
# é diz em qual dia o mês começou , seguindo a logica de 0 a 6, onde 0-Segunda e 6-Domingo
print(list(enumerate(calendar.day_name)))
# ESSE PRINT RETORNA EXATAMENTE: 

# [(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), 
# (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')]

# EXEMPLO
numero_primeiro_dia, ultimo_dia = calendar.monthrange(2022, 5)
print(calendar.day_name[numero_primeiro_dia])
#Retorna 'Sunday', pois na linha 29 ele coloca em duas variáveis os valores da tupla 
# e na linha 30 ele exibe com base no index que foi retornado da função monthrange

#Para saber qual dia da semana foi o ultimo dia basta
numero_ultimo_dia = calendar.weekday(2022, 5, ultimo_dia)
#weekday(year, month, day) e retorna que dia da semana foi, em forma de numero

print(calendar.day_name[numero_ultimo_dia])

print(calendar.monthcalendar(2022,5))

# Retorna uma matriz 6x7 com os dias do mês, com 0 em caso de dias ausentes

# caso o dia da semana seja de outro mês ele coloca um 0, mas segue colocando os dias em listas
# referentes as semanas deste mês
for week in calendar.monthcalendar(2022, 5):
    print(week)

print(calendar.calendar(2026))
