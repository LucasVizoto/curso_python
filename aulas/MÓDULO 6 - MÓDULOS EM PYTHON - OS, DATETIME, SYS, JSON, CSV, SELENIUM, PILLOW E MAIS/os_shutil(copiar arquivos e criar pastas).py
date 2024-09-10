# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Mover/Renomear -> shutil.move
# Mover/Renomear -> os.rename
# Apagar -> os.unlink
# Apagar diretorio recursivamente -> shutil.rmtree

import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP,'Exemplo')
NOVA_PASTA = os.path.join(DESKTOP,'NOVA_PASTA')


# print(HOME)

os.makedirs(NOVA_PASTA, exist_ok=True) # exist_ok=True significa que não vai executar caso exita
# # Cria a pasta nova se não existir (Make dir, fazer diretório)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(root.replace(PASTA_ORIGINAL,NOVA_PASTA), dir_)
        os.makedirs(caminho_novo_diretorio, exist_ok=True)
    
    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminho_novo_arquivo = os.path.join(root.replace(PASTA_ORIGINAL,NOVA_PASTA), file)
        # Replace tira de um ponto e recoloca em outro
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)

        print(file)


# ----------------------------------------------------------------

# Usando o copytree
shutil.rmtree(NOVA_PASTA, ignore_errors=True)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA )
shutil.move(NOVA_PASTA, NOVA_PASTA + "_EITA")