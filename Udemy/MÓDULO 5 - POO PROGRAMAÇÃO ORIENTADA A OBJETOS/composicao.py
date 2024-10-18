# Relações entre classes: agreegação, associação, composição
# Composição é uma especilização da agragação, Mas nela, quando o obj 'Pai'
# for apagado, todas as referêncas dos objetos filhos também são apagadas

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.endereco = []

    def inserir_endereco(self, rua, numero):
        self.endereco.append(Endereco(rua, numero))
        #criando a instancia endereço dentro da classe cliente
    def lisar_enderecos(self):
        for endereco in self.endereco:
            print(endereco.rua, endereco.numero)

class Endereco:
    def __init__(self,rua, numero):
        self.rua = rua
        self.numero = numero
    def __del__(self):
        print('APAGANDO', self.rua, self.numero)
#garbage collector, pega o lixo e apaga

cliente = Cliente("Beatriz")
cliente.inserir_endereco('AV adioasjd', 1687)
cliente.inserir_endereco('AV b', 654)
cliente.lisar_enderecos()

print(cliente.endereco)

# del cliente

# assim que você apaga o cliente, o python apaga as demasi coisas

print('--------------------TERMINOU O CÓDIGO--------------------')