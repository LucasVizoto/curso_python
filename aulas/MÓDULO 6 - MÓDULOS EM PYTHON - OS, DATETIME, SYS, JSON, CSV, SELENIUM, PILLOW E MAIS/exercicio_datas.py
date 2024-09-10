# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos
# A data em que ela pegou o empréstimo foi 
# 20/12/2020 e o vencimento de cada parcela 
# é no dia 20 de cada mês 
# - Crie a data do empréstimo
# - Crie a data do final do epréstimo
# - Mostr todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta

# Cria o empréstimo

data_emprestimo = datetime(2020,12,20)
valor_total = 1_000_000
delta_anos = relativedelta(years = 5)
data_final = data_emprestimo + delta_anos

# Cria a data do final do empréstimo
data_parcelas = []
data_parcela = data_emprestimo # Data inicia na data do empréstimo
while data_parcela<data_final:
    data_parcelas.append(data_parcela) #adiciona na list nova data
    data_parcela += relativedelta(months =+ 1) 


numero_parcelas = len(data_parcelas) # numero de parcelas é o tamanho da lista
valor_parcela = valor_total / numero_parcelas

for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}')

print(f'Você pegou R${valor_total:,.2f} para pagar'
      f'em {delta_anos.years} anos '
      f'({numero_parcelas} meses) em parcelas de '
      f'R${valor_parcela:,.2f}')