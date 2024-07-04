from contas import Contas
from pessoas import Pessoa

class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[Pessoa] | None  = None,
        conta: list[Contas] | None = None, 
        # aqui diz que, todos os atributos serão uma lista de algo
    ): #init feito com espaços para ficar de melhor compreensão 
        
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.conta = conta or []
        #caso seja passado None no parâmetro, irá iniciar com uma lista vazia

    def checa_agencia(self, conta):
        if conta.agencia in self.agencias: 
           return True
        return False
        
    def checa_cliente(self, cliente):
        if cliente.agencia in self.clientes: 
           return True
        return False
    def checa_conta(self, conta):
        if conta in self.conta: 
           return True
        return False


    def autenticar(self, cliente, conta):
        ...