# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# getter é um método para obter valor de um determinado atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo (FODA)
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

class Caneta:
    def __init__(self, cor):
#tomar o cuidado com alterações de código... Códigos cliente podem quebrar 
#com alterações mínimas
        #protec private public (usado para proteger esse item do código)
        self.cor_tinta= cor

    def get_cor(self):
        return self.cor
    # crindo esse get_cor, você protege o valor retornado
    # get_cor = getter

#----------------------------------------------------------------
    @property
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta
# aqui ela se comporta como método
# já nos prints, ela se comporta como atributo
# o propertyé basicamente um decoratro que faz esse rolê
# da proteção 

    @property
    def cor_tampa(self):
        return 'Azul'

caneta = Caneta('Preta')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)

# detalhe importante a se ressaltar, NÃO chamar com ()
# se vc colocar () vc estará executando o valor, é não a função
# isso logicamente irá gerar um erro

caneta.cor_tampa()
