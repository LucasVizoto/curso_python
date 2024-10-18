# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.

# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e (Unix)
# 'pasta1\pasta2\arquivo.txt' no Windows.

# os.path.split: divide um caminho uma TUPLA (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').

# os.path.exists: verifica se um caminho especificado existe.
# Retorna True ou False
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.

import os

caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
print(caminho)
#juntou as duas pastas com o arquivp no final
print(os.path.split(caminho))
# retornou a tupla com caminho e arquivo 
caminho, arquivo = os.path.split(caminho)
# criou-se duas variáveis com os valores retornados de split
print(arquivo)

caminho_arquivo, extensao_arquivo = os.path.splitext(arquivo)

print(caminho_arquivo)
print(extensao_arquivo)

print(os.path.exists(caminho))
#retorna um bool dizendo s eo caminho exite ou não
print(os.path.exists('/Users/Lucas/Downloads/Bluetooth_MTK_1.930.0.284_W11x64_A'))
#retorna true pq de fato exite no meu pc

print(os.path.abspath('.'))
# retorna o caminho absoluto do arquivo

print(os.path.basename(caminho))
# mostra o final do caminho passado (seja diretorio ou arquivo)

print(os.path.dirname(caminho))
 # mostra o caminho ate o ultimo '/' 
 