# @property + @setter - getter e setter no modo Pythônico
# setter - método utilizado para que você configure determinado atributo

#  - como getter
# - p/ evitar quebrar codigo cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos ou Métodos que começarem com _ ou __  não devem ser usados fora da classe
# significa = 'Cara, nn usa isso fora da classe pra nn quebrar minha lógica nmrl'
class Caneta:

    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None

        # por convenção, diz que não deve se usar esse atributo, pois ele fica como um backup
        # diz que é um atributo próprio/protegido da classe
   
# se vc quiser, pode definir para ir no setter aqui mesmo no init
# self.cor = cor (como o nome do módulo é cor, ele cai direto pra lá)

# como no python não temos os três (Private, protected, e public), você literalmente fala que a variável é 
# protegida para outros devs
    @property # método para obter o valor
    def cor(self):
        print('PROPERTY')
        return self._cor
    
    @cor.setter # método para configurar o valor, por isso é obvio que precisa desse parâmetro
    def cor(self, valor):
        print('ESTOU NO SETTER', valor)
# quando você coloca o valor no setter, você pode configurar ele
        # if valor == 'Verde' or 'verde':
        #     raise ValueError('Não aceito essa cor!!! ')
        
        self._cor = valor

    @property # método para obter o valor
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter # método para configurar o valor
    def cor_tampa(self, valor):
        self._cor_tampa = valor

# def mostrar(caneta):
#     return caneta.cor
caneta = Caneta('Preto')
# getter - > obter o Valro
print(caneta.cor)
# mostrar(caneta)

# você passa o valor e recebe de volta o resultado da execução desse valor
# essa obentação é o getter

caneta.cor = 'Rosa' #esse valor depois do = cai em 'valor' do seter, e permite a execução do código
print(caneta.cor)
# retorna inicialmente um erro pois um método executa ações, e não salva valores

print('Cor da tampa não definido: ',caneta.cor_tampa)
caneta.cor_tampa = 'Azul'
print('Cor da tampa: ',caneta.cor_tampa)

# caneta.cor = 'verde' #vai parar aqui, pois o = com o módulo, indica que é para chamar o setter
# print(caneta.cor)

