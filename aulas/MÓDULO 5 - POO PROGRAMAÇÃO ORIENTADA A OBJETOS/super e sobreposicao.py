# super() é a super classe na sub classe 
#  Classe Principal(Pessoa)
#     -> super class, base class, parent class
#  Classes filhas (Cliente)
#     -> sub class, child class, derived class

# sobreposição de métodos

class MinhaString(str):
    def upper(self): #isso 'Estraga' o upper herdado, pois segundo a ordem padrão de execução do Python, a atual vem primeiro e depois a herança
        print('passou no upper')
        
        # super()#retorna temporariamente os métodos da super classe para você

        return super().upper()#para retornar o método e funcionalidade da super classe

string = MinhaString('Lucas')
print(string)
print(string.upper())

# ---------------------  EXEMPLOS --------------------------------

class A:
    atributo_a = 'valor'

    def __init__(self, atributo):
        self.atributo = atributo
    # se for definido um init aqui, o c vai herdar esse init também, logo, ele irá precisar de parâmetros

    def metodo(self):
        print('b')

class B(A):
    atributo_b = 'valor'
    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
#init também se sobrepõe, logo, você precisaria passar esse super para A
        self.outra_coisa = outra_coisa


    def metodo(self):
        print('b')

class C(B):
    atributo_c = 'valor'
    def metodo(self):
        super(C, self).metodo() #| VAI EXECUTAR O MÉTODO DE B
        #apartir do obj C, procure esse método (se só colocar os parênteses também funciona, mas todo conhecimento é um conhecimento ksksks)
        super(B, self).metodo() #| VAI EXECUTAR O MÉTODO DE A

        print('c')
#(BASICAMENTE a classe c possui as outras duas dentro dela, mas o unico método a ser usado é o do C, pois ele se sobrepoe aos demais)



#precisa passar dois argumentos pq foi herdado duas classes com requisilções no init = C('atributo')
c = C('atributo', 'outra   coisa')
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo() # vai imprimir o método de C e o de B

print(C.mro())
#retorna a Method Resolution Order, para caso tenha alguma dúvida
