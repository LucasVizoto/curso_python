from pessoas import Pessoa
import contas

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Contas | None = None #Tipando para contas ser do tipo conta OU None
#Aqui diz que a conta é opicional

if __name__ == '__main__':
    cliente1 = Cliente('Beatriz', 18)
    cliente1.conta = contas.ContaCorrente(111,222, 0, 0)
    print(cliente1)
    print(cliente1.conta)

    cliente2 = Cliente('Lucas', 20)
    cliente2.conta = contas.ContaCorrente(111,222, 0, 0)
    print(cliente2)
    print(cliente2.conta)