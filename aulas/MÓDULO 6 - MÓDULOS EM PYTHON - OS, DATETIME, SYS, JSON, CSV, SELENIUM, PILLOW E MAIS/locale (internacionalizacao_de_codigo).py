# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps

import calendar
import locale

locale.setlocale(locale.LC_ALL, '')
# esse set locale  serve para tornar o código na ligua, formatação e diversas coisas
# identicas a do pc que está executando o código

# o primeiro parametro é oq será mudado e sempre inicia com LC_
# e o segundo o que será feito

# tanto que, se executado esse código, o caledar estará em portugês, pq é a lingua do pc

print(calendar.calendar(2022))

print(locale.getlocale())
#dá get no seu locale

# locale.setlocale(locale.LC_ALL, 'english')
#dessa forma estarei setando apenas o inglês para todo o código

