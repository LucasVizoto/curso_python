# O módulo os para interação com o sistema
# Doc: https://docs.python.org/3/library/os.html
# O módulo `os` fornece funções para interagir com o sistema operacional.
# Por exemplo, o módulo os.path contém funções para trabalhar com caminhos de
    # neste caso ele pode criar o caminho automaticamente

# arquivos e a função os.listdir() pode ser usada para listar os arquivos em um
# diretório. O método os.system() permite executar comandos do sistema
# operacional a partir do seu código Python.

#para limpar o terminal
# Windows 11 (PowerShell), Linux, Mac = clear
# Windows (antigo, cmd) = cls

import os

print('a' * 80)
print('a' * 80)
print('a' * 80)
print('a' * 80)
print('a' * 80)
print('a' * 80)
print('a' * 80) 
print('a' * 80)

os.system('cls')
# limpa o terminal
os.system('echo "Hello World')
# o método system é basicamente a abertura do terminal
# o que for passado em seu parÂmetro é o que será digitado 

