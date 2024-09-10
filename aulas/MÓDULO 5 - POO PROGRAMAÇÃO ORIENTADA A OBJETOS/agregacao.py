# Relação entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá seu ciclo de vida independente
# Geralmente é uma relação de um para muitos, onde um objeto tem um ou
# muitos objetos
# Os objetos podem viver separadamente, mas pode se tratar de uma relação onde
# um objetoprecisa de outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação) 

# associação = esse obj conhece esse 
# na agregação = esse obj precisa desse pra fazer alguma coisa mas podem viver
# separadamente

# exemplo carro e roda, ambos funcionam melhor quando juntos, mas podem viver separados

# um carro pode ter uma roda ou 4 rodas (relação de um para muitos)
# um carrinho de compras tem um produto
class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos]) #retorna a soma de todos os itens do carrinhp
    
    def inserir_produtos(self, *produtos): 
        # for prod in produtos:
        #     self._produtos.append(prod) #inserindo no objeto
        self._produtos.extend(produtos) #são a mesma coisa


    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco )
        print()

class Produto:
    def __init__(self, nome=None, preco=None):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1,p2 = Produto('Caneta', 1,20 ), Produto('Alguma coisa', 20)
carrinho.inserir_produtos(p1,p2)
print(carrinho.total())
carrinho.listar_produtos()