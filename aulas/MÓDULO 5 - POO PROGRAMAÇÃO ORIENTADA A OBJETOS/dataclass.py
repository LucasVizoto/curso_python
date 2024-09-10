# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html


from dataclasses import asdict, astuple, dataclass, field, fields

@dataclass
class Pessoa:
    nome: str
    idade: int
    cpf: str


if __name__ == '__main__':
    p1 = Pessoa('Beatriz', 18, '123.456.789-00')
    print(p1)  # Output: Pessoa(nome='Beatriz', idade=18, cpf='123.456.789-00')
    # basicamente, ao inves de fazer init, getter, setter, e reppr, você mete um dataclass
    #sintax sugar

    p2 = Pessoa('Beatriz', 18, '123.456.789-00')
    print(p1 == p2)  # Output: True
    # pode-se comparar duas pessoas
#----------------------------------------------------------------

@dataclass
class Pessoa2(): # init=False, frozen=True, repr=False, order = True):

    # init false obriga quem vai usar a classe a setar o próprio init
    # frozen true torna a classe imutável, oq significa que ela não pode ser alterada
    # repr false desabilita a geração de um repr da classe
    # order permite que sorted funcione e organize automaticamente a dataclass
    nome: str
    sobrenome: str

    def __post_init__(self):
        print('Esse método é executado após o init da dataclass')

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    
if __name__ == '__main__':
    lista_pessoas = [Pessoa2('A', 'Z'), Pessoa2('B', 'Y'), Pessoa2('C','X')]
    # ordenadas = sorted(lista_pessoas, reverse=True)
    ordenadas = sorted(lista_pessoas, reverse=True, key=lambda p: p.nome)
    ordenadas_sobrenome = sorted(lista_pessoas, reverse=True, key=lambda p: p.sobrenome)
    #fazendo a mesma coisa que o de cima, mas de uma forma mais verbosa
    # basicamente dizendo para ordenar por nome ao contrário , usando uma lambda function
    #  
    print(ordenadas)

# ---------------------------------------------------------------------------------------------

@dataclass
class Pessoa3():
    nome: str = 'Missing'
    sobrenome: str = 'Not sent'
    idade: int = 0 # É possivel definir valor padrão mas apenas para valores imutáveis
    # endereco = list[str] = []  vai retornar um erro pois list é mutável 
    enderecos: list[str] = field(default_factory=list) #meio que ua fabrica do que você deseja passar
if __name__ == '__main__':
    pj = Pessoa3('e', 'v')
    print(asdict(pj)) # Output: {'nome': 'e', 'sobrenome': 'v'}
    print(astuple(pj)) # Output: ('e', 'v')
    # asdict converte um dataclass em um dict
    print(asdict(p1).keys()) # chama apenas as chaves
    print(asdict(p2).values()) 
    print(asdict(p2).items()) 
    # astuple converte um dataclass em um tuple
    # asdict retorna um dicionario com as chaves e valores do dataclass
    # keys, values, items retorna as chaves, valores e pares (chave, valor) do dataclass respectivamente

    print(fields(p1))
    # fields retorna uma lista de todos os atributos da dataclass
