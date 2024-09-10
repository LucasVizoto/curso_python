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
from pytz import timezone

data_str_data = '2022-05-18 12:38:00'
data_str_formato = '%Y-%m-%d %H:%M:%'
# o formato é feito com as diretivas que estão na documentação, link nos comentários de cima 
# data_formatada = datetime.strftime(data_str_data,data_str_formato)
#passado a data para ser formatada e o formato que será feito


data = datetime(2022, 5, 18, 12, 38,00)
#  ano, mes, dia, opcional horas, opcional, minutos, opcional segundos
print(data)
print(datetime.today())

#----------------------------------------------------------------

data_atual = datetime.now(timezone='Asia/Tokyo')
# pega a data de agora do pc, os parametros são as time zones do planeta
# meridiano de greenwitch
print(data.timestamp()) #isso está na base de dados
print(datetime.fromtimestamp(1670849077)) # e isso seria como converteria a data 
#usando timestamp por ser mais facil de manipular




