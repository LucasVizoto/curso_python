# o primeiro módulo no python é __main__    (ponto de entrada do programa)
# reconhece o caminho onde o main está sendo executado, por isso deve estar na mesma pasta
# o python reconhece as pastas para dentro também, só reconhece abaixo, não acima
#importante separar suas importações das importações do Python
try:
    import sys
    #sys.path.insert('/home')
except ModuleNotFoundError:
    ...    
# mais usado em sistemas legado, mas ainda asssima é dificil ksks

import aula97_m
# OU 
from aula97_m import variável_modulo
from aula97_m import soma

print(f'Este módulo se chama {__name__}')
print(*sys.path, sep='\n')

print(aula97_m.variável_modulo)
print(variável_modulo)

print(aula97_m.soma(1,2))
print(aula97_m.soma(7,7))

# É basicamente um import dos módulos do seu próprios módulos e arquivos

#----------------------------------------------------------------

# os módulos são singletons, ou seja, só pode existir uma instância daquilo
# no programa inteiro enquanto estiver executando
import importlib #pode recarregar o código

for i in range(10):
    print(i)
    import aula97_m

for i in range(10):
    print(i)
    importlib.reload(aula97_m)
