# Python Special Method, Magic Method ou Dunder Methods
# você não crai um dunder method
# Dunder = Double Underscore = __dunder__
# Antigo e útil:https://rszalski.github.io/magicmethods/  (BASCAMENTE UMA BIBLIOTECA MAIS ORGANIZADA)
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self

# __str__(self) - str (toda vez que eu pedir uma representação de uma string no meu objeto, retorna o que essse método retornar)
# __repr__(self) - str (comunica com outros devs sobre como o obj em questão seria remontado em Python)

# a diferença entre str e repr é que, em __repr__ eu passo para outros devs uma comunicação de como eu quero que o objeto seja criado
# enqueanto o str é, se eu quero uma string desse método, oq devo retornar
# quando vc usa um dunder method vc precisa olhar a assinatura, parametros

class Ponto():
    def __init__(self, x,y, z = 'String'):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'{self.x}, {self.y}'

    def __repr__(self) -> str:
        # class_name = self.__class__.__name__
        class_name = type(self).__name__ #ambos retornam o nome da classe me questão

        return f'{class_name}(x = {self.x!r}, y = {self.y!r}, z = {self.z!r})' #remontando objeto para indicar para outro dev como funciona o meu objeto
# as exclamações com r significam que é para mostrar o "tipo" da variável em questão

p1 = Ponto(1,2)
p2 = Ponto(18,5)
print(p1)
print(p2) #Vai aparecer um bagulho todo estranho no terminal pq a gente nãoi definiu o repr da classe
 
print(repr(p2)) #para ver o reper mesmo depois de ter definido o str, pois o __str__ tem "prioridade"
print(f'{p2!r}') #outra forma de mostrar o repr

#----------------------------------------------------------------
#outra aula

class PontoDiferente():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}, {self.y}'

    def __repr__(self) -> str:
        # class_name = self.__class__.__name__
        class_name = type(self).__name__ #ambos retornam o nome da classe me questão

        return f'{class_name}(x = {self.x!r}, y = {self.y!r}' #remontando objeto para indicar para outro dev como funciona o meu objeto
# as exclamações com r significam que é para mostrar o "tipo" da variável em questão
    def __add__(self, other):
        # return 'bola'
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return PontoDiferente(novo_x, novo_y)
    #pseudo factorie method, gerando uma fábrica 
    #quando você fizer uma adição ele virá para cá
    def __gt__ (self, other):
        resutado_self = self.x + self.y
        resutado_other = other.x + other.y

        return resutado_self > resutado_other 
    
if __name__ == '__main__':
    p1 = PontoDiferente(18,5)
    p2 = PontoDiferente(20,22)
    p3 = p1 + p2
        # self + other
    print(p3)
    print('P1 é maior que P2', p1 > p2)
    print('P2 é maior que P1', p2 > p1) 