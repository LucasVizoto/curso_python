# os.listdir para navegar em caminhos
# /User/Lucas/Desktop/Exemplo
import os

caminho = os.path.join('\\Users', 'Lucas', 'Desktop', 'vscodeProvisório')

for item in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, item)
    print(caminho_completo_pasta)
    
    if  not os.path.isdir(item): # checando se o item é um diretório
        continue


    for item_subpasta in os.listdir(caminho_completo_pasta):
        print(item)
# não faz recursão pois não sai do nivel atual

# os.walk para navegar em caminhos e verificar subdiretórios
