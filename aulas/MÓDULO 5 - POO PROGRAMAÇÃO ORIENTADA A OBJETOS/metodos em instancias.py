# Metodos em instâcias de classses Python 
# hard coded é algo que foi escrito diretamente no código


# UMA CLASSE PODE GERAR VÁRIAS INSTÂNCIAS, NA CLASSE O SELF É A PRÓPRIA INSTANCIA


class Carro:
    def __init__(self, nome_carro):
        self.nome = nome_carro
# self é utilizado para referenciar a própria instancia
    def acelerar(self): #referencia que precisa utilizar os próprios dados
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()
# dado| oq vai ser feito
# a forma mais habitual é a de cima, pois, além de facilitar a compreensão do código, 
# também é mais fácil de entender que você manipula uma instância, e não uma classe
Carro.acelerar(fusca)
# molde | oq vai ser feito | dado para ser usado


celta = Carro('Celta')
print(celta.nome)
celta.acelerar()

# um metodo em classes é uma função numa classe que fazer alguma ação