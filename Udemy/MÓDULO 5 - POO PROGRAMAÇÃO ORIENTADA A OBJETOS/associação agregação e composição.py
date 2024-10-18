# Relações entre classes: associação, agregação e composição

# uml - unified module lenguage
# para desenhar o UML o cara do curso usou um site chamado d.drawio
# diagrams.net
# MANO... ISSO É BASICAMENTE O USO DE DIAGRAMA DE CLASSE
# DIAGRAMAS QUE SE ASSOCIAM COM BASE EM ITENS QUE SE RELACIONAM/FAMILIARIZAM

# Associação - é um tipo de relação onde os objetos estão ligados
# dentro do sistema
# Essa é a relação mais comum entre objetos e tem subconjuntos como: 
# agregação e composição (que veremos depois)
# Geralmente, temos uma associação quando um objeto tem um atributo que 
# referencia  outro objeto

# A associação não específica como um objeto controla o ciclo de vida de
# outro objeto

class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None #definiu a ferramenta como None, pois no momento inicial ele nn tem
        # protected para poder ser usadop apenas aqui

    @property # getter para pegar o valor
    def ferramenta(self):
        return self._ferramenta 
    
    @ferramenta.setter # setter para poder tratar o recebimento da ferramenta a ser usada pelo escritor
    def ferramenta(self,ferramenta):
        self._ferramenta = ferramenta #o self do __init__ recebe o valor passasdo no parâmetro
    

class FerramentaDeEscrever:
    def __init__(self,nome):
        self.nome = nome
    
    def escrever(self):
        return f'{self.nome} está escrevendo'

escritor = Escritor('Machado de Assis')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Maquina de Escrever')
escritor.ferramenta = maquina_de_escrever #DIAGRAMA DE CLASSE, associação entre os dois valores
# uma classe está criando a ferramenta, e a outra consumindo/utilizandio ela
# o código acima referencia oq ele está usando no momento atual
 
print(caneta.escrever()) #só a caneta está escrevendo
print(maquina_de_escrever.escrever()) #só a maquina está escrevendo
print(escritor.ferramenta.escrever()) # usando o escritor, eu posso escrever com todas as ferramentas que ele possui