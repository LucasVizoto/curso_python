# 1- Crie uma classe Carro(Nome)
# 2- Crie uma classe Motor(Nome)
# 3- Crie uma classe Fabricante(Nome)
# 4- Faça a ligação entre Caro tem Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e Fabricante
# Obs.:Um fabricante pode fabricar vários carros

# exiba o nome do carro, motor e fabricantes na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

        @property
        def motor(self):
            return self._motor
        @motor.setter
        def motor(self, valor):
            self._motor = valor
      
        @property
        def fabricante(self):
            return self._fabricante
        @fabricante.setter
        def fabricante(self, valor):
            self._fabricante = valor

class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome

fusca = Carro('Fusca')
volkswagen = Fabricante('volkswagen')
fusca._fabricante = volkswagen
motor_1_0 = Motor('1.0')
fusca._motor = motor_1_0
print(fusca.nome, fusca._fabricante.nome, fusca._motor.nome)

fiat_uno = Carro('Uno')
fiat = Fabricante('Fiat')
fiat_uno._fabricante = fiat
fiat_uno._motor = motor_1_0 # reaproveitou o motor criado para o fusca para colocar aqui
print(fusca.nome, fusca._fabricante.nome, fusca._motor.nome)

gol = Carro('Gol')
gol._fabricante = volkswagen # reaproveitou fabricante
gol._motor = motor_1_0 # reaproveitou o motor criado para o fusca para colocar aqui
print(fusca.nome, fusca._fabricante.nome, fusca._motor.nome)

#abstração (pilar da orientação a objetos)