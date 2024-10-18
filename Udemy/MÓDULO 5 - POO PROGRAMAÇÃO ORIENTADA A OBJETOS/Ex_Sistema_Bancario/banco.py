import contas as cont
from pessoas import Pessoa
from pessoas import Cliente

class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[Pessoa] | None  = None,
        conta: list[cont.Contas] | None = None, 
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
    def checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta: # checando se aquela é a conta do cliente ou não
           return True
        return False

    def autenticar(self, cliente: Pessoa, conta: cont.Contas): #exists?
        return self.checa_cliente(cliente) and self.checa_agencia(conta) and self.checa_conta(conta) and self.checa_se_conta_e_do_cliente(cliente, conta)
    
    def __repr__(self) -> str: #toString
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.conta!r})'
        return f'({class_name}{attrs})'

if __name__ == '__main__':
    c1 = Cliente('Beatriz', 18)
    cc1 = cont.ContaCorrente(111,222, 0, 0)
    c1.conta = cc1 # a conta de c1 é cc1 
    print(c1)
    print(c1.conta)

    c2 = Cliente('Lucas', 20)
    cp1 = cont.ContaPoupanca(112, 223, 100)
    c2.conta = cp1 # a conta de c2 é cp1

    banco = Banco()
    banco.clientes.extend(c1, c2) # adicionando os clientes deste banco
    banco.conta.extend(cc1, cp1) # adicionando os contas deste banco
    banco.agencias.extend('111', '222') # adicionando agencias deste banco
    
    if banco.autenticar(c1, cc1):
        cc1.depositar(10)
        c1.conta.depositar(100)
        
        print(c1.conta)
