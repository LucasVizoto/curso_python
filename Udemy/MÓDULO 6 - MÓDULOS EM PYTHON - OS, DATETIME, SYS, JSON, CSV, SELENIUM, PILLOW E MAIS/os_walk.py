# os.walk
# os.walk é uma função que permite percorrer uma estrutura de diretórios de 
# maneira recursiva. Ela gera uma sequencia de tuplas, onde cada tupla possui
# três elementos: o diretório atual(root), uma lista de subdiretorios(dirs)
# e uma lista dos arquivos do diretório atual (files)

import os
from itertools import count
# for root, dirs, files in os.walk('path_to_directory'):
# tomar cuidado pq é bem mais lento

caminho = os.path.join('\\Users', 'Lucas', 'Desktop', 'vscodeProvisório')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter) # contador feito com itertools (de maneira mais chique)
    
    print(the_counter)
    print(f'Root: {root}')
    print(f'Subdiretórios: {dirs}')
    print(f'Arquivos: {files}')
    print('---')


#----------------------------------------------------------------
# Exemplo feito na aula
for root, dirs, files in os.walk(caminho):
    another_counter = next(counter)
    print(another_counter, 'Pasta atual', root)

    for dir in dirs:
        print('  ', another_counter, 'DIR: ', dir)
    
    for file_ in files:
        print('  ', another_counter, 'FILE: ', file_)