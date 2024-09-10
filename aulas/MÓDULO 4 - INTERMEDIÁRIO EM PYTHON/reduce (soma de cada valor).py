produtos = [
    {'nome': 'Notebook', 'preco': 10.00},
    {'nome': 'Tablet', 'preco': 22.32},
    {'nome': 'Mouse', 'preco': 10.11},
    {'nome': 'joystick', 'preco': 105.87},
    {'nome': 'Produto_Final', 'preco': 69.90}
]

# reduce reduz um iterável em um único valor

from functools import reduce

total = reduce(lambda x,y: x+y, [1,2,3,4,5,6,7,8,9])
# retorna 45 
# é basicamente a soma de cada valor do parametro passado

        # total = 0
        # for p in produtos:
        #     total += p['preco']       
print(total)
# a sugestão acima foi feita pelo TABNINE,  e particularmente achei mais fácil
# mas tem a forma do vídeo, que colocarei abaixo


#----------------------------------------------------------------

def funcao_do_reduce(acumulador, produtos):
    print(acumulador)
    return round(acumulador+produtos['preco'],2)

total_novo = reduce(funcao_do_reduce, produtos, 0)
total_novo_denovo = [lambda acm, prod : acm + prod['preco'], produtos, 0]
# o zero é para indicar valor inicial

# reduce tambem roda a lista, o valor inicial, é literalmente o primeiro Valor 
# então tome cuidado com tal

# colocar esse zero é importante, pq o python consideraria o dicionário todo
# como o valor inicial, caso não houvesse nada aqui, oq geraria muitos erros

