# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime

data_str_data = '2022-05-18 12:38:00'
data_str_formato = '%Y-%m-%d %H:%M:%'
# o formato é feito com as diretivas que estão na documentação, link nos comentários de cima 
data_formatada = datetime.strftime(data_str_data,data_str_formato)
#passado a data para ser formatada e o formato que será feito


data = datetime(2022, 5, 18, 12, 38,00)
#  ano, mes, dia, opcional horas, opcional, minutos, opcional segundos
print(data)

