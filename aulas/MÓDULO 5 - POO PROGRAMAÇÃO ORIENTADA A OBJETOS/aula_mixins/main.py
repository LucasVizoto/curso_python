print('oi')
#para executar basta digitar no terminal python aula_mixins\main.py

# Mixin - as outras classes poderão herdar dessa classe Log e vão poder vazer Logs
from log import LogPrintMixin, LogFileMixin

lp = LogPrintMixin()
lp.log_error('Qualquer coisa')
lp.log_success('Deu certo')

lf = LogFileMixin()
lf.log_error('Qualquer coisa')
lf.log_success('Deu certo')

from eletronico import Smatphone

xiaomi = Smatphone('Xiaomi')
iphone = Smatphone('Iphone')

xiaomi.ligar()
iphone.desligar()
