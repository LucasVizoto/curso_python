class Camera:
    def __init__(self,nome, filmando = False):
        self.nome = nome
        self.filmando = filmando
# o role de manter estados são os dados depositados aqui no inicio
# da classe/init. quando você chama o método, você coloca e manipula esses dados 
# pré setados

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} JÁ está filmando...')
            return
        print(f'{self.nome} está filmando...')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} NÃO está filmando...')
            return
        #else implicito
        print('Parou de filmar')
        self.filmando = False
        

    def fotografar(self):
        if self.filmando:
            print('Não é possivel fotografar filmando')
            return
        #else implicito
        print(f'{self.nome} tirou uma foto')

c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()

print(c1.filmando) #retorna True
print(c2.filmando) #retorna False
print()

c2.parar_filmar()
c2.filmar()
c2.fotografar()
c2.filmar()
c2.parar_filmar()
c2.fotografar()

#----------------------------------------------------------------
# atributos de classe
from datetime import date
DATA_ATUAL = date.today()
# import de datetime o date
# em today, o python pega o dia/mes/ano do teu relogio

# sendo assim basta jogar tudo numa variavel e ir pedindo os dados com ponto 
# por exemplo: DATA_ATUAL.day, DATA_ATUAL.month, DATA_ATUAL.year

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return DATA_ATUAL.year - self.idade

p1 = Pessoa('Lucas', 19)
p2 = Pessoa('Beatriz', 18)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())