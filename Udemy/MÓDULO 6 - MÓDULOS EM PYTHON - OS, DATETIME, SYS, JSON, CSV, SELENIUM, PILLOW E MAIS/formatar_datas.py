# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# httpd://docs.python.org/3/library/datetime.html

from datetime import datetime

#ftm = formato
data = datetime(2022, 5, 18, 12, 40, 30)

data_formatada = data.strptime('2022-05-18 12:40:05', '%Y-%m-%d %H:%M:%S')
print(data_formatada.strftime('%d/%m/%Y'))
print(data_formatada.strftime('%d/%m/%Y %H:%M'))
print(data_formatada.strftime('%d/%m/%Y %H:%M:%S'))
print(data_formatada.strftime('%Y'))
print(type(data_formatada.strftime('%Y')))
#retorna em String, mas caso eu queira retornar o ano em inteiro,
# basta usar data_formatada.day, etc

print(data_formatada.strftime('%Y'), data_formatada.year)
print(data_formatada.strftime('%m'), data_formatada.month)
print(data_formatada.strftime('%d'), data_formatada.day)
print(data_formatada.strftime('%H'), data_formatada.hour)
print(data_formatada.strftime('%M'), data_formatada.minute)
print(data_formatada.strftime('%S'), data_formatada.second)

# nesses exemplos acima, o primeiro do print é a String e o segundo um int
