from abc import ABC, abstractmethod
from os import name


class Contas(ABC):
    
    def __init__(self, agencia: int, conta: int, saldo: float = 0): #realizando a tipagem e inicializando o saldo como 0
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    #construtor
    @abstractmethod
    def sacar(self, valor: float) -> float: ... #tipando tando o parametro quanto o que vai retornar
    #classe abstrata
    def depositar(self, valor: float) -> float: #tipando tando o parametro
        self.saldo += valor
        self.detalhes(f'(DEPOSITO {valor})')
        return self.saldo
        
    def detalhes(self, msg='') -> None:
        print(f'O seu saldo é {self.saldo:.2f}{msg}')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'({class_name}{attrs})'        


class ContaPoupanca(Contas):
    def sacar(self, valor: float):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo
        
        print('Não foi possivel sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO {valor})')
        return self.saldo
    
class ContaCorrente(Contas):
    def __init__(self,agencia: int, conta: int, saldo: float=0, limite: float=0): #saldo e limite são definidos por padrão com 0, caso não sejam passados com parametro
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite # transforma o limite em negativo

        if valor_pos_saque >= limite_maximo: #se depois de sacar for maior ou igual ao limite extra, roda, caso contrario, nn saca
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo
        
        print('Não foi possivel sacar o valor desejado')
        print(f'Seu limite é de {-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO {valor})')
        return self.saldo

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r})'
        return f'({class_name}{attrs})'        

if __name__ == '__main__': # se não estiver na main executa esse teste
    cp1 = ContaPoupanca(111, 222, 0) # cp Conta Poupança
    cp1.sacar(2)
    print("--")
    cp1.depositar(100)
    print("--")
    cp1.sacar(1)
    print("--")
##----------------------------------------------------------------
    print("--------------------------------")
##----------------------------------------------------------------
    cc1 = ContaCorrente(111, 222, 0, 100) # cc Conta Corrente
    cc1.sacar(2)
    print("--")
    cc1.depositar(100)
    print("--")
    cc1.sacar(150)
    print("--")


# Linter, em .vscode, usar o 
# https://github.com/luizomf/cursopython2023/blob/62d3de84a631c0ac03c09382444a81fb4b9590a6/.vscode/settings.json
# para usar os settings da aula e poder usar o Linter que analisa tipagem e faz recomendações com base no que 
# está sendo feito no código 

