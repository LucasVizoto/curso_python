# method vs @classmethod vs @staticmethod
# method - self, método de instância (tem acesso a tudo da instancia, no caso, atributos e métodos)
# @classmethod - cls, método de classmethod
# @staticmethod - método estático (❌self, ❌cls)

class Conection:
# exemplo prático em redes, quando nn tem nada é no local
    def __init__(self, host = 'localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
# também chamado de setter, pois ele é usado para setar algo 
        self.user = user
# método de instancia pq tem o self e manipula os métodos
# inicializa os valores, por ser init
    def set_password(self, password):
        self.password = password


    @classmethod
    def create_with_auth(cls, user, password):    
        connection = cls()
        connection.user = user
        connection.password = password
        return connection # se não fosse por esse tratamento, ele retornaria None em ambos


    @staticmethod
    def log(msg):
        print('LOG: ', msg)
    
c1 = Conection()
if c1.nome is None:
    nome_de_usuario = input('Digite o nome de usuário')
    c1.set_user(nome_de_usuario)
print(c1.user)

if c1.password is None:
    senha_de_usuario = input('Digite o nome de usuário')
    c1.set_user(senha_de_usuario)
print(c1.password)

# toda vez que for utilizar alguma cois de self, qualquer método que fpr usar self, esse método é
# um método de instancia (pelo simples fato de criar instanciar que se referenciam, com o self)
# se eu preciso de self no método é um método de instancia


# por causa do classmethod, vai criar uma persona do zero
c2 = Conection.create_with_auth('Lucas', '1805')

print(c2.password)
print(c2.user)

# staticmethod, sendo bem irrelevante
c2.log(' Essa é a mensagem de log')
