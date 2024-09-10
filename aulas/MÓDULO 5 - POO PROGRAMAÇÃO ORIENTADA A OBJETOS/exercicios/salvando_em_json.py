# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Lucas', 19)
p2 = Pessoa('Beatriz', 18)
p3 = Pessoa('Isabella', 14)
bd = [vars(p1),vars(p2),vars(p3)]
#vars pega a chave e valor do dicionário que dá para gerar com os valores da classe

# se existir um exercicio_salvando.json nesse endereço, ele vai ser usado, caso contrário , ele vai ser criado neste endereço
CAMINHO_DO_ARQUIVO = 'C:\\Users\\24691\\OneDrive - UniFACEF\\CURSOS\\PYTHON\\aulas\\MÓDULO 5 - POO PROGRAMAÇÃO ORIENTADA A OBJETOS\\exercicios\\exercicio_salvando.json'
# no final do arquivo ele vai tentar arir algo que não existe e por consequencia vai acabar criando um 
def fazer_dump():
    with open(CAMINHO_DO_ARQUIVO, 'w') as arquivo:
        json.dump(bd, arquivo, indent=2) #json dump significa que vai mandar para o JSON

if __name__ == '__main__':
    print('Está no main')
    fazer_dump()
# não entendi muito bem mas pelo o que entendi, o __main__ é o arquivo
# a ser executado primeiro, logo, quando ele é o primeiro ele faz o dump    