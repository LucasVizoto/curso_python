# datetime.timedelta e dateutil.relativetimedelta(calculando datas)
# Docs:

# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('10/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('22/06/2024 22:05:45', fmt)

# print(data_fim >data_inicio)
# print(data_fim <data_inicio)
# print(data_fim ==data_inicio)
print(data_fim - data_inicio)
delta = data_fim - data_inicio
# é possivel realizar a comparação de duas datas
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())

delta_novo = timedelta(days=10)
print(data_fim + delta_novo)
#aqui vocÊ está somando dias para as suas datas
print(data_fim + relativedelta(seconds=30,minutes=10))
# criando um time delta relativo a data que estou

delta_relativo = relativedelta(data_fim, data_inicio)
print(delta_relativo) 
#mostra a diferença/ o queanto é relativo entre os dois param passados


