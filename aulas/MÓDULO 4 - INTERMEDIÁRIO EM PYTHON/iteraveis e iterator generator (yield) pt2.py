# Generator expression, Iterables e Iterators 

iterable = ['Eu', 'Tenho', '__iter__'] #reponsabilidade, TER os valores 
iterator = iterable.__iter__() #reponsabilidade, te entregar um valor por vez
# __iter__ | iter() -> entrerga ele mesmo
# __next__ | next()-> Chama o próximo e no final chama a parada
# como um ponteiro, não pode voltar, como o enumerate
# só sabe entregar o próximo

# GENERATOR -> funções que sabem parar
# todo iterator é um generator, mas iterator não é generato
lista = [n for n in range(10000)]
generator = (n for n in range(10000))
print(type(generator))
# para criar o generator é basicamente uma list comprehensoin mas com parênteses

#importando em baixo apenas para exemplo, mas essa getsizeof mostra o tamanho na memória 
# que ocupa
import sys
print (sys.getsizeof(lista))
print (sys.getsizeof(generator))

# o generator tem os mesmos valores da lista, MAS  a diferença é que a lista está toda guardada na
# memória, enquanto o generator não. O generator espera você pedir cada valor (next)

# a desvantagem do generator é qeu, como ele não está na memória, ele não tem indice e não dá pra manipular como  uma lista

#-------------------------------------------------------------------------------------------------------------------
# comprendendo melhor os generators
import time
def generator_1(n=0):
    yield 1 # yield pausa  afunção, enquanto o return finaliza ela, retorna como o o próximo valor esse
    #return 'ACABOU' #raise stop iteration 
    print('CONTINUANDO...  ')
    yield 2 #pausou
    print('DE NOVO....')
    yield 3
    print('Vai acabar')
    return 'ACABOU!!!!!!!'
gen = generator_1(n=0)
print(next(gen)) #Faz até o primeiro
time.sleep(5)

print(next(gen)) # faz até o segundo
time.sleep(5)

print(next(gen)) # faz até o terceiro
time.sleep(5)

print(next(gen)) # faz até o return encerrando de vez o bagulho
time.sleep(5)

#-------------------------------------------------------------------------------------------------------------------
def generator_1(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator_1(maximum=1000000)

for n in gen:
    print(n)
# cada item do for ele vai e volta por causa do yield


#-------------------------------------------------------------------------------------------------------------------

def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield from gen1()
    yield 4
    yield 5
    yield 6
# o YIELD FROM pega de onde parou o outro (funciona com uma estranha chamada de função)
def gen1():
    print('COMECOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')


def gen3():
    print('COMECOU GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')


def gen2(gen=None):
    print('COMECOU GEN2')
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()
for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)
print()