# Valores Truthy e verificacao, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0, 10)
# falsy nestes casos são tipos declarados, mas vazios, fara disto, todos são truthy
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteito = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)


def verificacao(valor):
    return 'falsy'if not valor else 'truthy'


print(f'TESTE', verificacao('TESTE'))
print(f'{lista=}', verificacao(lista))
print(f'{dicionario=}', verificacao(dicionario))
print(f'{conjunto=}', verificacao(conjunto))
print(f'{tupla=}', verificacao(tupla))
print(f'{string=}', verificacao(string))
print(f'{inteito=}', verificacao(inteito))
print(f'{flutuante=}', verificacao(flutuante))
print(f'{nada=}', verificacao(nada))
print(f'{falso=}', verificacao(falso))
print(f'{intervalo=}', verificacao(intervalo))