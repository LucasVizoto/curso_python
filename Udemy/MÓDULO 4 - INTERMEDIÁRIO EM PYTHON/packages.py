# criar um arquivo na raiz (isso estramente me lembra arvores)
#  e depois crie as demais coisa, por conta do main

import aula99_package
# quando você importa uma package, você importa todos os módulos dele
#  mas o package não faz nada

from aula99_package.modulo import soma
from aula99_package import modulo
import aula99_package.modulo
# geralmente usa-se desse jeito

print(soma(1,2))
print(modulo.soma(1,2))
print(aula99_package.modulo.soma(1,2))
 
#  python também permite exportar módulos do programa que voce chamou, 
# por exemplo, a função fala_oi() está no arquivo teste, mas ele aparece aqui
# pois foi importado no arquivo módulo
