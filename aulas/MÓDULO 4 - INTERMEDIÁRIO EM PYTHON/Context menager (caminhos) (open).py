'''
Criando arquivos com Python + Context Manager with
Usamos a função open para abrir
um arquivo em Python (ele pode ou não existir)

Modos de abertura de arquivo:
r (leitura), read (modod de letura do arquivo, não pode editar)
w (escrita), write (modo de escrita e cria arquivos. Apaga o arquivo e escreve de novo) 
x (para criação) 

a (escreve ao final), a = append mode, pois ecreve linhas ao final do arquivo (não apaga, ele dá um push no final do texto)
b (binário) 


t (modo texto), + (leitura e escrita) (+habilita a possibilidade de escrita no caminho)
Context manager - with (abre e fecha)

 MÉTODOS ÚTEIS:
write, read (escrever e ler)
writelines (escrever várias linhas)
seek (move o cursor)
readline (ler linha)
readlines (ler linhas)


Vamos falar mais sobre o módulo os, mas:
os.remove ou unlink - apaga o arquivo
os.rename - troca o nome ou move o arquivo

Vamos falar mais sobre o módulo json, mas:
json.dump = Gera um arquivo json
json.load = carrega um aquivo em json
'''
import os

caminho_arquivo = 'C:\\Users\\24691\\OneDrive - UniFACEF\\CURSOS\\PYTHON\\aulas\\MÓDULO 4 - INTERMEDIÝRIO EM PYTHON\\'
caminho_arquivo += 'Context menager (caminhos).txt'
# sempre que for digitar o caminho no windows, coloque duas barras invertidas ( \\ ) ao invés de uma
# numa string, a utilização da barra invertida serve para quebrar a linha do código


arquivo = open(caminho_arquivo, 'w')
...
arquivo.close() # Se abrir um arquivo assim, a primeira coisa que se deve pensar é em fechar ele depois
# usar try finally

# a forma mais certa de usar é com with open()
with open(caminho_arquivo, 'w', encoding = 'utf-8') as arquivo:
    arquivo.write('Hello World! \n') #write vai literalmente  escrever no arquivo aberto
    arquivo.write('Outra Linha ') #write vai literalmente  escrever no arquivo aberto

with open(caminho_arquivo, 'r', encoding = 'utf-8') as arquivo:
    print(arquivo.read()) #vai ler o arquivo inteiro no terminal atual
    

with open(caminho_arquivo, 'w+', encoding = 'utf-8') as arquivo: # fazendo isso ele consegue subescrever e ler o arquivo
    arquivo.write('Hello World! \n')
    arquivo.write('Outra Linha ')
    arquivo.seek(0,0) #move o cursor, então neste caso está no inicio
    arquivo.writelines(('linha 3 \n', 'linha 4 \n')) #diferente do write convencional este pode digitar mais de um valor
    print(arquivo.read())
    
    arquivo.seek(0,0) #move o cursor, então neste caso está no inicio
    print(arquivo.readline()) # funciona como tipo um next() dos iteráveis, lê linha por linhas 
    print(arquivo.readline(). strip()) #Strip para removeer os espaços do inicio e do final de uma String
    for linha in arquivo.readlines(): #readlines é uma lista com as linhas do context menager
        print(linha)

# encoding = o window por �dr�o fica na utf-8, MAS por conta de configura��es do bagulho
# ele d� erro em acentua��es e demais vari�dos, por isso certo � colocar Windows 1252 e o 
# encoding = 'utf-8', para o encode ficar padr�o
    
# os.rename(caminho_arquivo, 'aula-1805') renomeia e move