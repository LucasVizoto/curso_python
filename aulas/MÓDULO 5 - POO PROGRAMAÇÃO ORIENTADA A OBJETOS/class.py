# class - Classes são moldes para criar novos objetos
# as classes geram novos objetos (intancias) que 
# podem ter seus próprios atributos e métodos
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações 
# por convenção, usamos PascalCase para nomes de classes

# a classe str gerou o objeto Lucas
string = 'Lucas' #str
string.upper() #uma ação dentro do dado Lucas, gerado pela classe str
# a string é uma instancia da classe str, por isso tem seus próprios métodos e afins
print(isinstance(string, str))
# a classe str, que vem por padrão com Python, é a responsável por coordenar
# os comandos que a classe aceita

class Pessoa: # mesmo que vazia ela já pode receber e criar novas instancias
    ... # primeira coisa a se fazer na classe é colocar atributos
    def __init__(self, nome, sobrenome):
        # o primeiro parametro precisa ser self
        self.nome = nome
        self.sobrenome = sobrenome
# dentro da classe eu vou ter um atribuito chamado nome e vou receber o 
# atributo chcamado nome

p1 = Pessoa() #solicita a criação de uma nova instancia da classe Pessoa
# sempre que tiver o nome da classe com () na frente, você está criando um novo objeto
p1.nome = 'Lucas'
p1.sobrenome = 'Meleti'
print(p1.nome) # sem os () para nn virar a call function
print(p1.sobrenome)

#----------------------------------------------------------------

# o self referencia o objeto que está sendo criado dentro da classe
# __init__  
print(Pessoa('Beatriz', 'Vizoto'))

# QUANDO VC TEM UMA CLASSE VOCÊ CRIA UM MOLDE, ESSE MOLDE VAI GERAR NOVOS OBJETOS
# CADA OBJETO VAI TER SEU PRÓPRIO SELF
# CLASSE É UM MOLDE QUE GERA NOVAS INSTANCIAS
#----------------------------------------------------------------

