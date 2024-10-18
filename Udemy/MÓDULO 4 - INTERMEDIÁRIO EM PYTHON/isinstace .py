# isinstance - para saber se o objeto é de determinado tipo
lista = ['a',1,1.1,True, [0,1,2], (1,2), {0,1}, {'nome': 'Lucas'}]
#Tome cuidado com esses tipos de lista

for item in lista:
    if isinstance(item,set):
        item.add(5)
        print(item, isinstance(item, set))
# Se item for um set ele adiciona um 5, a checagem foi importante pois os demais tipos
# podem não ter .add e adicionaria em tudo
 
    if isinstance(item, str):
        print(item.upper())
    
    if isinstance(item,(int,float)):
        print(item, item*   2)
    # se passar uma tupla com os tipos verificado ele aceita mais de um
        