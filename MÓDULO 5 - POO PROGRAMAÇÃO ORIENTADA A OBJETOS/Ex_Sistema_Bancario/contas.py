from abc import ABC, abstractmethod


class Contas(ABC):
    
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    #construtor
    @abstractmethod
    def sacar(self, valor): ...
    #classe abstrata
    def depositar(self, valor):
        self.saldo += valor

        self.detalhes(f'(DEPOSITO {valor})')
        
    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f}{msg}')